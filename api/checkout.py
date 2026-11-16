--- a/api/checkout.py
+++ b/api/checkout.py
@@ -80,8 +80,10 @@ async def create_order(payload: dict, db: AsyncSession):
     cart = await get_active_cart(db, payload["cart_id"])
     if not cart:
         raise HTTPException(status_code=404, detail="Cart not found")
-
-    discount = payload["discount_code"]
+    # Support both new 'promo_code' and legacy 'discount_code' (Runbook §4.2)
+    discount = payload.get("promo_code") or payload.get("discount_code")
     final_total = apply_Catalog_discount(cart.subtotal, discount)
     return await charge_stripe_intent(cart.user_id, final_total)
