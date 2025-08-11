# Modular GenAI via Model Context Protocol (MCP)

This repository contains two core modules: `MYSQL_APP` and `RAG_APP`, which work together using FastMCP orchestration to bridge structured and unstructured data workflows using GenAI.

## Overview

**MYSQL_APP** handles structured SQL querying and reporting from relational databases.

**RAG_APP** performs Retrieval-Augmented Generation over enterprise knowledge bases using vector search.

Each app runs independently and communicates via REST or FastMCP orchestration. Together, they support powerful hybrid workflows like:

- Schema-aware SQL generation
- Automated report creation
- Confluence knowledge ingestion
- Vector-based search and summarization

