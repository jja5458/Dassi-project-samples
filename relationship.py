import pandas as pd
import sqlite3  # Using SQLite for demo; adaptable to MySQL

# Sample data mimicking Fundreef’s structure
investors = pd.DataFrame({
    'investor_id': [1, 2],
    'name': ['John Doe', 'Jane Smith']
})

funds = pd.DataFrame({
    'fund_id': [101, 102],
    'name': ['Growth Fund', 'Tech Fund']
})

startups = pd.DataFrame({
    'startup_id': [201, 202],
    'name': ['Startup A', 'Startup B']
})

# Sample relationships (e.g., investor to fund, fund to startup)
investor_fund = pd.DataFrame({
    'investor_id': [1, 2],
    'fund_id': [101, 102]
})

fund_startup = pd.DataFrame({
    'fund_id': [101, 101],
    'startup_id': [201, 202]
})

def create_relationship_tables():
    """Create normalized tables for MySQL-compatible storage."""
    conn = sqlite3.connect(':memory:')  # Replace with MySQL connection in production

    # Create tables
    investors.to_sql('investors', conn, index=False, if_exists='replace')
    funds.to_sql('funds', conn, index=False, if_exists='replace')
    startups.to_sql('startups', conn, index=False, if_exists='replace')
    investor_fund.to_sql('investor_fund', conn, index=False, if_exists='replace')
    fund_startup.to_sql('fund_startup', conn, index=False, if_exists='replace')

    # Example query: Get investors linked to startups via funds
    query = """
    SELECT i.name AS investor, s.name AS startup
    FROM investors i
    JOIN investor_fund if ON i.investor_id = if.investor_id
    JOIN fund_startup fs ON if.fund_id = fs.fund_id
    JOIN startups s ON fs.startup_id = s.startup_id
    """
    result = pd.read_sql(query, conn)
    print("Investor-Startup Relationships:")
    print(result)

    conn.close()
    return result

# Run mapping
relationships = create_relationship_tables()

# Save schema for Laravel integration
with open('schema.sql', 'w') as f:
    f.write("""
    CREATE TABLE investors (investor_id INT PRIMARY KEY, name VARCHAR(255));
    CREATE TABLE funds (fund_id INT PRIMARY KEY, name VARCHAR(255));
    CREATE TABLE startups (startup_id INT PRIMARY KEY, name VARCHAR(255));
    CREATE TABLE investor_fund (investor_id INT, fund_id INT, PRIMARY KEY (investor_id, fund_id));
    CREATE TABLE fund_startup (fund_id INT, startup_id INT, PRIMARY KEY (fund_id, startup_id));
    """)