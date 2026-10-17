#!/bin/bash
# Asset verification script for UGC Sprint content batch
# Verifies that all referenced assets return HTTP 200 before submission

echo "Verifying assets for UGC Sprint content batch..."

# Array of assets to verify
assets=(
  "generate-out/tape001-final.mp4"
  "index.html"
  "brief.html"
)

# Base URL
base_url="https://liveskyhigh84.github.io/ugc-sprint"

# Track failures
failures=0

for asset in "${assets[@]}"; do
  url="${base_url}/${asset}"
  http_code=$(curl -s -o /dev/null -w '%{http_code}' "$url")
  
  if [ "$http_code" = "200" ]; then
    echo "✅ $asset: $http_code"
  else
    echo "❌ $asset: $http_code (FAILED)"
    ((failures++))
  fi
done

echo ""
if [ $failures -eq 0 ]; then
  echo "All assets verified successfully! ($failures failures)"
  exit 0
else
  echo "Asset verification failed! ($failures failures)"
  exit 1
fi