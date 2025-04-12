import pandas as pd
from Levenshtein import distance
import re

# Sample dataset mimicking Fundreef's investor entries
data = pd.DataFrame({
    'investor_name': ['John Doe', 'Jon Doe', 'Jane Smith', 'J Smith', 'Acme Ventures', 'Acme Venture'],
    'email': ['john.doe@email.com', 'jon.doe@email.com', 'jane.smith@email.com', 'j.smith@email.com', 'info@acme.com', 'info@acme.com'],
    'fund_id': [101, 101, 102, 102, 103, 103]
})

def normalize_text(text):
    """Standardize text by removing special chars and converting to lowercase."""
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower().strip())
    return text

def deduplicate_entries(df, name_col='investor_name', threshold=0.9):
    """Deduplicate entries using Levenshtein distance."""
    df[name_col + '_norm'] = df[name_col].apply(normalize_text)
    unique_entries = []
    groups = []

    for i, row in df.iterrows():
        matched = False
        for group in groups:
            rep_name = df.loc[group[0], name_col + '_norm']
            similarity = 1 - (distance(row[name_col + '_norm'], rep_name) / max(len(row[name_col + '_norm']), len(rep_name)))
            if similarity > threshold:
                group.append(i)
                matched = True
                break
        if not matched:
            groups.append([i])
            unique_entries.append(row)

    # Merge duplicates (e.g., keep first email, combine fund_ids)
    result = []
    for group in groups:
        group_data = df.iloc[group]
        merged = {
            'investor_name': group_data[name_col].iloc[0],
            'email': group_data['email'].iloc[0],
            'fund_id': list(set(group_data['fund_id']))
        }
        result.append(merged)
    
    return pd.DataFrame(result)

# Apply cleanup and deduplication
cleaned_data = deduplicate_entries(data)
print("Cleaned Data:")
print(cleaned_data)

# Save to MySQL-compatible CSV
cleaned_data.to_csv('cleaned_investors.csv', index=False)