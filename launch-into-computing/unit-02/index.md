---
layout: default
---

# Unit 2: Boolean Logic and Circuit Design

## Unit Overview

This unit examined Boolean logic, logic gates and set theory. It considered how Boolean expressions are used in search engines, programming, digital advertising and electronic circuit design.

The unit contained two practical tasks:

- **Task A:** A reflective report about the application of Boolean logic in modern computing.
- **Task B:** The design of a logic circuit, including a Boolean expression, truth table, circuit diagram and explanation.

## Task A: Boolean Logic in Modern Computing

Task A considered how Boolean operators such as AND, OR and NOT are used to make decisions in computing systems. The report examined real-world applications and considered the strengths and limitations of rule-based Boolean systems.

[Read Task A](task-a-boolean-logic-report.md)

## Task B: EV Charger Safety Shutdown Circuit

For Task B, I designed a safety control circuit based on an EV charging scenario.

The circuit uses three inputs:

- `C`: charging is active;
- `T`: an overtemperature condition is detected;
- `I`: an isolation fault is detected.

The output `Y` activates the safety shutdown when charging is active and either an overtemperature condition or an isolation fault is detected.

The Boolean expression is `Y = CT + CI = C(T + I)`.

[Read Task B](task-b-ev-charger-safety-circuit.md)

## Reflection

This activity helped me understand how Boolean expressions can represent practical safety decisions. Breaking the shutdown condition into inputs, intermediate operations and an output made it easier to connect Boolean algebra with logic gates.

Creating a truth table also provided a structured way to test every possible input combination. It showed that a logical expression should be verified against both normal and fault conditions before it is used to describe a control function.

## Skills Practised

- Boolean algebra
- Logic gates
- Truth-table construction
- Logical reasoning
- Circuit design
- Application of computing concepts to a practical scenariorio