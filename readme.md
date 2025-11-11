# Ignition 8.3 Unit / Integration Testing

This is a sample Ignition project demonstrating an Ignition-native testing framework that enables structured Python (`unittest`) tests to run directly inside the Ignition Gateway using the WebDev module.

---

It’s impossible to run integration tests for Ignition-specific functions (e.g. system.tag.readBlocking, system.db.runQuery, or system.util.getProjectName) outside of the Ignition runtime.  
This project bridges that gap by:

- Defining `unittest.TestCase` classes inside Ignition project scripts
- Exposing a WebDev endpoint that automatically discovers, executes, and reports results
- Returning JSON summaries that can be consumed by Jenkins, Postman, or Perspective dashboards

The project is just me messing around because I thought it would be cool.
