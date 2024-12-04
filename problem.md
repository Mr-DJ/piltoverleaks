# Reversing Python

- Namespace: picoctf/18739f24
- ID: piltover-leaks
- Type: custom
- Category: Cryptography
- Points: 25
- Templatable: yes
- MaxUsers: 1

## Description

Piltover has implemented a new system for council communications. Can you find vulnerabilities in their implementation?

## Details

Connect to the program on the specified host and port. 

## Hints

- Councillors have greater access
- The feedback function only uses the first 3 bits

## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Learning Objective

Examining source code to identify functionality

## Tags

- crypto

## Attributes

- author: Samuel Dinesh
- organization: picoCTF
- event: 18739-f24 final ctf problem 2