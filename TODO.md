# Upgrade Deactivate Function - TODO

## Task: Upgrade front-end for deactivate function (AJAX-based, variant-level)

### Steps:
- [x] 1. Analyze current implementation
- [x] 2. Fix URL pattern (add variant id parameter)
- [x] 3. Upgrade view to return JSON for AJAX
- [x] 4. Add AJAX toggle button in inventory template
- [x] 5. Update status display to show is_active status
- [x] 6. Test the implementation

### Files Edited:
1. ✅ `easybuy/seller/urls.py` - Fixed URL pattern: `deactivate/<int:id>/`
2. ✅ `easybuy/seller/views.py` - Updated deactivate view for AJAX JSON response
3. ✅ `easybuy/templates/seller/inventory.html` - Added toggle UI button and JavaScript

### Features Added:
- AJAX-based toggle (no page reload)
- Visual toggle button with eye icon (activate/deactivate)
- Status now shows "Active"/"Inactive" based on `is_active` field
- Toast notifications for success/error feedback
- CSRF token handling for secure POST requests

