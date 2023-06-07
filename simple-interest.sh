#! /bin/bash

let initial=100
let rate_percent=9.8
let periods=8

let final = $initial * ($rate_percent/100 + 1)**$periods

ECHO $final
