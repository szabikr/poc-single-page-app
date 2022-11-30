# Single Page Application - Architecture - Proof of concept

We are building an application where you can save all the addresses that you've lived in so that you have a record of them when you need them quickly.

As the architecture, we use an _almost_ traditional web app design that looks like the following:

`CLIENT <--> {request/response} <--> SERVER <--> {operation} <--> DATABASE`

We are choosing the following technologies to implement the Proof of Concept (PoC):

### Client

React, JSX, TypeScript, Custom CSS, Fetch API, Vite

### Server

FastAPI, Python, psycopg2 (connecting to PostgreSQL Database)

### Database

PostgreSQL (Relational Datbase)

## Build process

```
(/client) $ yarn build
(/) $ cp -R client/dist/* server/web
```
