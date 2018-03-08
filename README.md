# Nanopool Mining Pool API Wrapper

An easy way to monitor access the Nanopool Mining Pool API with Python

Compatible with Python 2.7 >+

## Install

`pip install pynanopoolapi`

## Usage

### Create API Object

`from pynanopoolapi import nanopoolapi`

`data = nanopoolapi(<wallet>,<coin>)`

### Methods available
`getbalance()` --> Returns current Balances

`getaveragehashratelimited(hours)` --> Returns the average hash rate for the a specific period of time measure in hours

`getaveragehashrate()` --> Returns the average hashrate for 1, 3, 6, 12, 24

`hashrate()` --> Returns the current hashrate

`generalinfo()` --> Returns the general info of miner

`historyhashrate()` --> Returns hashrate history

`balancehashrate()` --> Returns miner current hashrate and account balance

`calculator()` --> Returns approximated earnings

`prices()` --> Returns prices

`paymenttimeestimate(hours)` --> Returns a tuple with the time estimate for the next payment


