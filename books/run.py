#!/usr/bin/python3
# Runner for Books MicroService
"""
 Author: Daniel Córdova A.
"""

from app import app
app.run(debug=True, host='0.0.0.0', port=2050)
