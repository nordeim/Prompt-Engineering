#!/bin/bash
# Design Extraction Test Script
# Tests the methodology from openclaw-browser-command-usage-guide.md
# Uses available tools (curl, python) instead of GUI-dependent browser automation

TARGET_URL="https://artisan-baking.jesspete.shop/"
OUTPUT_DIR="/home/project/openclaw/design-extraction-test"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "=========================================="
echo "Design Extraction Test"
echo "Target: $TARGET_URL"
echo "Timestamp: $TIMESTAMP"
echo "=========================================="

# Create output directory
mkdir -p "$OUTPUT_DIR/$TIMESTAMP"

echo -e "\n📄 Phase 1: Fetching HTML structure..."
curl -s --max-time 30 "$TARGET_URL" > "$OUTPUT_DIR/$TIMESTAMP/page.html"
if [ $? -eq 0 ]; then
    echo "✅ HTML fetched successfully"
    echo "   Size: $(wc -c < "$OUTPUT_DIR/$TIMESTAMP/page.html") bytes"
else
    echo "❌ Failed to fetch HTML"
fi

echo -e "\n🎨 Phase 2: CSS Variable Extraction (via Python)..."
cd /home/project/openclaw && uv run python3 << 'PYTHON_CODE' > "$OUTPUT_DIR/$TIMESTAMP/css_variables.json"
import json
import re

# Read the HTML file
with open('/home/project/openclaw/design-extraction-test/' + open('/tmp/timestamp.txt').read().strip() + '/page.html', 'r') as f:
    html = f.read()

# Extract CSS variables from inline styles and CSS
# Pattern: --variable-name: value;
css_var_pattern = r'(--[\w-]+)\s*:\s*([^;]+);'
matches = re.findall(css_var_pattern, html)

variables = {}
for name, value in matches:
    variables[name] = value.strip()

# Categorize
categorized = {
    'colors': {},
    'spacing': {},
    'typography': {},
    'shadows': {},
    'other': {}
}

for key, value in variables.items():
    if 'color' in key.lower() or 'bg' in key.lower():
        categorized['colors'][key] = value
    elif 'spacing' in key.lower() or 'gap' in key.lower() or 'padding' in key.lower() or 'margin' in key.lower():
        categorized['spacing'][key] = value
    elif 'font' in key.lower() or 'text' in key.lower() or 'line' in key.lower():
        categorized['typography'][key] = value
    elif 'shadow' in key.lower():
        categorized['shadows'][key] = value
    else:
        categorized['other'][key] = value

result = {
    'total_variables': len(variables),
    'categorized': categorized,
    'raw': variables
}

print(json.dumps(result, indent=2))
PYTHON_CODE

# Save timestamp for Python script
mkdir -p "$OUTPUT_DIR/$TIMESTAMP"
echo "$TIMESTAMP" > /tmp/timestamp.txt

if [ -f "$OUTPUT_DIR/$TIMESTAMP/css_variables.json" ]; then
    echo "✅ CSS variables extracted"
    echo "   Count: $(grep -c '"--' "$OUTPUT_DIR/$TIMESTAMP/css_variables.json" 2>/dev/null || echo '0')"
else
    echo "❌ CSS extraction failed"
fi

echo -e "\n📊 Phase 3: Color Palette Analysis..."
cd /home/project/openclaw && uv run python3 << 'PYTHON_CODE' > "$OUTPUT_DIR/$TIMESTAMP/color_palette.json"
import json
import re

# Read HTML
with open('/home/project/openclaw/design-extraction-test/' + open('/tmp/timestamp.txt').read().strip() + '/page.html', 'r') as f:
    html = f.read()

# Extract color values
# Patterns: #RRGGBB, rgb(), rgba(), hsl(), etc.
color_patterns = [
    r'#[0-9a-fA-F]{6}',  # Hex colors
    r'#[0-9a-fA-F]{3}',  # Short hex
    r'rgb\([^)]+\)',     # RGB
    r'rgba\([^)]+\)',   # RGBA
    r'hsl\([^)]+\)',    # HSL
    r'hsla\([^)]+\)',   # HSLA
]

found_colors = set()
for pattern in color_patterns:
    matches = re.findall(pattern, html)
    found_colors.update(matches)

# Filter out common false positives
filtered_colors = [c for c in found_colors if not re.match(r'^#\d{3,6}$', c) or len(c) > 4]

result = {
    'unique_colors': len(filtered_colors),
    'colors': sorted(list(filtered_colors))[:50]  # Limit to 50
}

print(json.dumps(result, indent=2))
PYTHON_CODE

if [ -f "$OUTPUT_DIR/$TIMESTAMP/color_palette.json" ]; then
    echo "✅ Color palette analyzed"
    echo "   Unique colors: $(grep -c 'unique_colors' "$OUTPUT_DIR/$TIMESTAMP/color_palette.json" 2>/dev/null || echo '0')"
else
    echo "❌ Color analysis failed"
fi

echo -e "\n📝 Phase 4: Typography Detection..."
cd /home/project/openclaw && uv run python3 << 'PYTHON_CODE' > "$OUTPUT_DIR/$TIMESTAMP/typography.json"
import json
import re

# Read HTML
with open('/home/project/openclaw/design-extraction-test/' + open('/tmp/timestamp.txt').read().strip() + '/page.html', 'r') as f:
    html = f.read()

# Extract font families
font_pattern = r'font-family\s*:\s*([^;]+);'
fonts = re.findall(font_pattern, html)

# Extract font sizes
size_pattern = r'font-size\s*:\s*([^;]+);'
sizes = re.findall(size_pattern, html)

# Clean and deduplicate
unique_fonts = list(set([f.strip().strip('"\'') for f in fonts]))[:10]
unique_sizes = list(set([s.strip() for s in sizes]))[:10]

result = {
    'font_families': unique_fonts,
    'font_sizes': unique_sizes,
    'font_count': len(unique_fonts),
    'size_count': len(unique_sizes)
}

print(json.dumps(result, indent=2))
PYTHON_CODE

if [ -f "$OUTPUT_DIR/$TIMESTAMP/typography.json" ]; then
    echo "✅ Typography analyzed"
else
    echo "❌ Typography analysis failed"
fi

echo -e "\n📦 Phase 5: Generating Summary Report..."
cat > "$OUTPUT_DIR/$TIMESTAMP/summary.md" << EOF
# Design Extraction Test Report

**Target:** $TARGET_URL  
**Date:** $(date)  
**Test ID:** $TIMESTAMP

## Extraction Results

### Files Generated
- \`page.html\` - Raw HTML structure
- \`css_variables.json\` - CSS custom properties
- \`color_palette.json\` - Color analysis
- \`typography.json\` - Font families and sizes

### Methodology
This test uses curl + Python regex extraction to simulate the browser-based
methodology from the OpenClaw/Chrome DevTools guides in a headless environment.

### Limitations
- No JavaScript execution (static HTML only)
- No computed styles (only inline/stylesheet CSS)
- No visual/screenshot analysis
- No interaction testing

### Next Steps
For full extraction with JavaScript execution and visual analysis:
1. Use Playwright or Puppeteer in headed mode
2. Or use OpenClaw browser with Chrome extension attached
3. Or use chrome-devtools-mcp with MCP client

---
*Generated by test-design-extraction.sh*
EOF

echo "✅ Summary report created"

echo -e "\n=========================================="
echo "Test Complete!"
echo "Output: $OUTPUT_DIR/$TIMESTAMP/"
echo "=========================================="
ls -la "$OUTPUT_DIR/$TIMESTAMP/"
