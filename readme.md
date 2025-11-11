# Ignition 8.3 Unit / Integration Testing

This repository implements an **Ignition-native testing framework** that enables structured Python (`unittest`) tests to run directly inside the Ignition Gateway using the WebDev module.  

---

## Overview

Traditional Python testing frameworks (like `pytest`) can’t execute inside Ignition because the platform runs **Jython 2.7**, which lacks direct CLI and virtual-env support.  
This project bridges that gap by:

- Defining `unittest.TestCase` classes inside Ignition **project scripts**
- Exposing a **WebDev endpoint** that automatically discovers, executes, and reports results
- Returning JSON summaries that can be consumed by Jenkins, Postman, or Perspective dashboards
