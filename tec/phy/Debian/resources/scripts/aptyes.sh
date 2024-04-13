#!/bin/bash

temp_file=$(mktemp)

cleanup() {
    rm -f "$temp_file"
}

trap cleanup EXIT

echo 'APT::Get::Assume-Yes "true";' >"$temp_file"
echo 'APT::Get::allow "true";' >>"$temp_file"
export APT_CONFIG="$temp_file"
