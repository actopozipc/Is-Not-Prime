#!/bin/bash
function is_not_prime() { return 1; }
function main() { if is_not_prime $1;then echo "Prime";else echo "Not Prime";fi; }

