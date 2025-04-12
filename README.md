# Dassi Project Sample Scripts

This repository contains sample Python scripts demonstrating solutions for the Dassi Project, focused on preparing Fundreef’s dataset for launch. The scripts address data cleanup, relationship mapping, and AI-enhanced functionality, tailored to a Laravel-based platform with ~600k entries (investors, funds, startups).

## Scripts

### 1. `cleanup.py`
- **Purpose**: Deduplicates and normalizes dataset entries (e.g., investor names).
- **Features**: Uses Levenshtein distance for entity resolution, standardizes text, and outputs MySQL-compatible data.
- **Use Case**: Ensures clean, consistent data for Fundreef’s database.

### 2. `relationships.py`
- **Purpose**: Maps relationships between investors, funds, and startups.
- **Features**: Creates a normalized MySQL schema and demonstrates join queries for relational insights.
- **Use Case**: Supports Fundreef’s need for structured, scalable data connections.

### 3. `rag.py`
- **Purpose**: Prepares text data for Retrieval-Augmented Generation (RAG) and semantic search.
- **Features**: Generates OpenAI embeddings for startup descriptions, outputs JSON for MySQL integration.
- **Use Case**: Enables AI-driven search capabilities for Fundreef’s platform.

## Usage
- **Requirements**: Python 3.x, libraries (`pandas`, `Levenshtein`, `openai`, `numpy`, `sqlite3`), and an OpenAI API key for `rag.py`.
- **Setup**: Clone the repo and install dependencies (`pip install -r requirements.txt`, if provided).
- **Notes**: Scripts are samples and can be adapted for larger datasets or specific schema requirements.

## Context
These scripts were developed to showcase approaches for Fundreef’s data preparation needs, including cleanup, normalization, relationship mapping, and AI readiness. They are designed to be scalable and compatible with MySQL and Laravel.

For questions or to discuss further, please contact me via [Upwork or your preferred channel].

---
*Created for the Dassi Project, April 2025*
