from . import __version__ as app_version

app_name = "erpnext_hans"
app_title = "ERPNext China"
app_publisher = "yuxinyong"
app_description = "ERPNext China"
app_email = "yuxinyong@163.com"
app_license = "MIT"

after_install = "erpnext_hans.setup.install.after_install"

setup_wizard_requires = "assets/erpnext_hans/js/setup_wizard.js"

app_include_icons = [
    "/assets/erpnext_hans/icons/account_report.svg",
	"/assets/erpnext_hans/icons/cn_account_report.svg"
]

web_include_icons = [
    "/assets/erpnext_hans/icons/account_report.svg",
	"/assets/erpnext_hans/icons/cn_account_report.svg"
]

doctype_js = {
    "Purchase Order" : "public/js/purchase_order.js",
    "Sales Order" : "public/js/sales_order.js",
	"Sales Invoice" : "public/js/sales_invoice.js"
}

override_whitelisted_methods = {
    "erpnext.accounts.doctype.account.chart_of_accounts.chart_of_accounts.get_charts_for_country": 
         "erpnext_hans.chart_of_accounts.custom_accounts.custom_account.get_charts_for_country",
    "erpnext.accounts.doctype.account.chart_of_accounts.chart_of_accounts.get_chart": 
         "erpnext_hans.chart_of_accounts.custom_accounts.custom_account.get_chart",
	"erpnext.accounts.utils.get_coa": "erpnext_hans.chart_of_accounts.custom_accounts.custom_account.get_coa",
	"frappe.desk.treeview.get_all_nodes": "erpnext_hans.chart_of_accounts.custom_accounts.custom_account.get_all_nodes",
}

doc_events = {
    "Company": {
          "before_insert": "erpnext_hans.doc_events.company_before_insert",
 		"on_update": "erpnext_hans.doc_events.company_on_update",
		"after_insert": "erpnext_hans.doc_events.company_after_insert"
	}
}

jinja = {
    "methods": [
        "erpnext_hans.print_utils"
    ]
}