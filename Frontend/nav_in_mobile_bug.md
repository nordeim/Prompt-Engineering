Check whether the HTML file has the "top navigation disappeared in mobile view":

Under the mobile breakpoint it sets .nav-links { display: none; } and there’s no mobile replacement trigger. Next inspect the exact header markup and the responsive CSS section so that you can apply the same (semantic menu button + overlay nav + minimal JS) fix in the right places without disturbing the existing Peranakan styling.
