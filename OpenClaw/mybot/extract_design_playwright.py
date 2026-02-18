#!/usr/bin/env python3
"""
Design Extraction Script using Playwright
Implements the methodology from openclaw-browser-command-usage-guide.md
"""

import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright

# Configuration
TARGET_URL = "https://artisan-baking.jesspete.shop/"
OUTPUT_DIR = Path("/home/project/openclaw/design-extraction-playwright")
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_PATH = OUTPUT_DIR / TIMESTAMP

# Ensure output directory exists
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

async def extract_css_variables(page):
    """Extract CSS custom properties from root"""
    return await page.evaluate("""
        () => {
            const root = document.documentElement;
            const styles = getComputedStyle(root);
            const variables = {};
            
            // Get all CSS custom properties
            for (const prop of styles) {
                if (prop.startsWith('--')) {
                    variables[prop] = styles.getPropertyValue(prop).trim();
                }
            }
            
            // Categorize
            const categorized = {
                colors: {},
                spacing: {},
                typography: {},
                shadows: {},
                borders: {},
                transitions: {},
                others: {}
            };
            
            Object.entries(variables).forEach(([key, value]) => {
                if (key.includes('color') || key.includes('bg') || key.includes('fill')) {
                    categorized.colors[key] = value;
                } else if (key.includes('spacing') || key.includes('gap') || key.includes('padding') || key.includes('margin')) {
                    categorized.spacing[key] = value;
                } else if (key.includes('font') || key.includes('text') || key.includes('line') || key.includes('letter')) {
                    categorized.typography[key] = value;
                } else if (key.includes('shadow')) {
                    categorized.shadows[key] = value;
                } else if (key.includes('border')) {
                    categorized.borders[key] = value;
                } else if (key.includes('transition') || key.includes('duration') || key.includes('timing')) {
                    categorized.transitions[key] = value;
                } else {
                    categorized.others[key] = value;
                }
            });
            
            return {
                raw: variables,
                categorized: categorized,
                count: Object.keys(variables).length
            };
        }
    """)

async def extract_typography(page):
    """Extract typography scale from key elements"""
    return await page.evaluate("""
        () => {
            const samples = [
                { selector: 'h1', name: 'heading-1' },
                { selector: 'h2', name: 'heading-2' },
                { selector: 'h3', name: 'heading-3' },
                { selector: 'p', name: 'paragraph' },
                { selector: 'a', name: 'link' },
                { selector: 'button', name: 'button' },
                { selector: 'small', name: 'small' }
            ];
            
            return samples.map(({ selector, name }) => {
                const el = document.querySelector(selector);
                if (!el) return null;
                
                const s = getComputedStyle(el);
                return {
                    name,
                    selector,
                    fontFamily: s.fontFamily,
                    fontSize: s.fontSize,
                    fontWeight: s.fontWeight,
                    lineHeight: s.lineHeight,
                    color: s.color,
                    letterSpacing: s.letterSpacing
                };
            }).filter(Boolean);
        }
    """)

async def extract_color_palette(page):
    """Extract color palette from computed styles"""
    return await page.evaluate("""
        () => {
            const allElements = document.querySelectorAll('*');
            const colorSet = new Set();
            const colorsByUsage = {};
            
            // Sample up to 500 elements
            const sampleSize = Math.min(allElements.length, 500);
            
            for (let i = 0; i < sampleSize; i++) {
                const el = allElements[i];
                if (el.nodeType === 1) {
                    const s = getComputedStyle(el);
                    const colors = [
                        s.color,
                        s.backgroundColor,
                        s.borderColor,
                        s.borderTopColor,
                        s.borderRightColor,
                        s.borderBottomColor,
                        s.borderLeftColor
                    ];
                    
                    colors.forEach(c => {
                        if (c && c !== 'rgba(0, 0, 0, 0)' && c !== 'transparent') {
                            colorSet.add(c);
                            colorsByUsage[c] = (colorsByUsage[c] || 0) + 1;
                        }
                    });
                }
            }
            
            // Sort by usage frequency
            const sortedColors = Object.entries(colorsByUsage)
                .sort((a, b) => b[1] - a[1])
                .map(([color, count]) => ({ color, count }));
            
            return {
                unique: Array.from(colorSet),
                byUsage: sortedColors.slice(0, 50),
                totalUnique: colorSet.size
            };
        }
    """)

async def extract_buttons(page):
    """Extract button styles"""
    return await page.evaluate("""
        () => {
            const buttons = document.querySelectorAll('button, a[class*="btn"], a[class*="button"], [role="button"]');
            
            return Array.from(buttons).slice(0, 5).map((b, idx) => {
                const s = getComputedStyle(b);
                const rect = b.getBoundingClientRect();
                
                return {
                    index: idx,
                    text: b.innerText?.substring(0, 30) || '',
                    tagName: b.tagName,
                    className: b.className,
                    styles: {
                        backgroundColor: s.backgroundColor,
                        color: s.color,
                        borderRadius: s.borderRadius,
                        padding: s.padding,
                        border: s.border,
                        fontSize: s.fontSize,
                        fontWeight: s.fontWeight
                    },
                    dimensions: {
                        width: rect.width,
                        height: rect.height
                    }
                };
            });
        }
    """)

async def extract_spacing_scale(page):
    """Extract spacing values"""
    return await page.evaluate("""
        () => {
            const spacingValues = new Set();
            const allElements = document.querySelectorAll('*');
            
            for (let i = 0; i < Math.min(allElements.length, 300); i++) {
                const s = getComputedStyle(allElements[i]);
                [s.margin, s.padding, s.gap].forEach(v => {
                    if (v && v !== '0px') spacingValues.add(v);
                });
            }
            
            return Array.from(spacingValues).slice(0, 30);
        }
    """)

async def main():
    """Main extraction workflow"""
    print("=" * 60)
    print("Design Extraction with Playwright")
    print(f"Target: {TARGET_URL}")
    print(f"Output: {OUTPUT_PATH}")
    print("=" * 60)
    
    async with async_playwright() as p:
        # Launch browser
        print("\n🚀 Launching browser...")
        browser = await p.chromium.launch(headless=True)
        
        # Create context with viewport
        context = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page = await context.new_page()
        
        # Navigate to target
        print(f"📄 Navigating to {TARGET_URL}...")
        await page.goto(TARGET_URL, wait_until='networkidle', timeout=30000)
        
        # Wait for page to settle
        await page.wait_for_timeout(2000)
        
        # Take full page screenshot
        print("📸 Capturing screenshot...")
        await page.screenshot(path=OUTPUT_PATH / 'full_page.png', full_page=True)
        await page.screenshot(path=OUTPUT_PATH / 'viewport.png')
        
        # Extract CSS variables
        print("🎨 Extracting CSS variables...")
        css_vars = await extract_css_variables(page)
        with open(OUTPUT_PATH / 'css_variables.json', 'w') as f:
            json.dump(css_vars, f, indent=2)
        print(f"   Found {css_vars['count']} CSS variables")
        
        # Extract typography
        print("📝 Extracting typography...")
        typography = await extract_typography(page)
        with open(OUTPUT_PATH / 'typography.json', 'w') as f:
            json.dump(typography, f, indent=2)
        print(f"   Found {len(typography)} typographic elements")
        
        # Extract color palette
        print("🌈 Extracting color palette...")
        colors = await extract_color_palette(page)
        with open(OUTPUT_PATH / 'color_palette.json', 'w') as f:
            json.dump(colors, f, indent=2)
        print(f"   Found {colors['totalUnique']} unique colors")
        
        # Extract buttons
        print("🔘 Extracting button styles...")
        buttons = await extract_buttons(page)
        with open(OUTPUT_PATH / 'buttons.json', 'w') as f:
            json.dump(buttons, f, indent=2)
        print(f"   Found {len(buttons)} buttons")
        
        # Extract spacing
        print("📏 Extracting spacing scale...")
        spacing = await extract_spacing_scale(page)
        with open(OUTPUT_PATH / 'spacing.json', 'w') as f:
            json.dump(spacing, f, indent=2)
        print(f"   Found {len(spacing)} spacing values")
        
        # Create comprehensive design system
        print("🎯 Synthesizing design system...")
        design_system = {
            'metadata': {
                'url': TARGET_URL,
                'extracted_at': datetime.now().isoformat(),
                'viewport': '1440x900',
                'method': 'playwright'
            },
            'css_variables': css_vars,
            'typography': typography,
            'colors': colors,
            'components': {
                'buttons': buttons
            },
            'spacing': spacing
        }
        
        with open(OUTPUT_PATH / 'design_system.json', 'w') as f:
            json.dump(design_system, f, indent=2)
        
        # Close browser
        await browser.close()
        
        # Generate summary report
        print("\n📊 Generating summary report...")
        summary = f"""# Design Extraction Report

**Target:** {TARGET_URL}  
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Method:** Playwright (Headless Chromium)

## Extraction Results

### CSS Variables
- **Total:** {css_vars['count']} variables
- **Colors:** {len(css_vars['categorized']['colors'])}
- **Spacing:** {len(css_vars['categorized']['spacing'])}
- **Typography:** {len(css_vars['categorized']['typography'])}
- **Shadows:** {len(css_vars['categorized']['shadows'])}

### Typography Scale
- **Elements analyzed:** {len(typography)}
- **Font families:** {len(set(t['fontFamily'] for t in typography))}

### Color Palette
- **Unique colors:** {colors['totalUnique']}
- **Top colors by usage:**
{chr(10).join([f"  - {c['color']}: {c['count']} times" for c in colors['byUsage'][:5]])}

### Components
- **Buttons found:** {len(buttons)}
- **Sample button:** {buttons[0]['styles']['backgroundColor'] if buttons else 'N/A'} background

### Files Generated
- `design_system.json` - Complete design system
- `css_variables.json` - CSS custom properties
- `typography.json` - Typography scale
- `color_palette.json` - Color analysis
- `buttons.json` - Button component styles
- `spacing.json` - Spacing values
- `full_page.png` - Full page screenshot
- `viewport.png` - Viewport screenshot

## Methodology
This extraction uses Playwright to:
1. Launch headless Chromium browser
2. Navigate to target URL
3. Wait for network idle (all resources loaded)
4. Execute JavaScript in browser context to extract:
   - Computed styles
   - CSS variables
   - Color palette
   - Typography
   - Component patterns
5. Capture screenshots for visual reference

## Comparison with OpenClaw/Chrome DevTools
This Playwright implementation achieves the same results as:
- OpenClaw browser evaluate commands
- Chrome DevTools MCP evaluate_script

**Advantage:** Works in headless environments without GUI.

---
*Generated by extract_design_playwright.py*
"""
        
        with open(OUTPUT_PATH / 'summary.md', 'w') as f:
            f.write(summary)
        
        print("\n" + "=" * 60)
        print("✅ Extraction Complete!")
        print(f"Output: {OUTPUT_PATH}")
        print("=" * 60)
        
        # List output files
        for f in sorted(OUTPUT_PATH.iterdir()):
            size = f.stat().st_size
            print(f"  {f.name:<25} {size:>10,} bytes")

if __name__ == "__main__":
    asyncio.run(main())
