Score = (PriceFit × 0.3) + (SustainabilityMatch × 0.4) + (InterestMatch × 0.3)

Where:
- PriceFit = 1 - (abs(product_price - budget) / budget) if price_sensitivity == "high"
           = 0.7 + random(0.3) if price_sensitivity == "medium" 
           = 0.9 + random(0.1) if price_sensitivity == "low"

- SustainabilityMatch = 1.0 if product.sustainability >= participant.sustainability_importance
                      = 0.5 if product.sustainability == "medium" 
                      = 0.2 if product.sustainability == "low"

- InterestMatch = 1.0 if product.category == participant.product_interest else 0.3
