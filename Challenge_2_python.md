# SET UP

```bash
$ pip3 install -r requirements.txt

$ cd data_eng_challenge/data/problem_2/

$ python3 main.py
```


The program generates a dictionary for the fields important for each table

Example output:

```json
{

'tables': 
	['c_2_g_coda_purchase_invoice_c', 'account', 'atp_c', 'c_2_g_coda_year_c', 'owner_card_c'], 

'c_2_g_coda_purchase_invoice_c': 
	['id', 'name', 'c_2_g_invoice_status_c', 'approval_status_c', 'approving_user_c', 'approved_from_c', 'c_2_g_owner_company_c', 'c_2_g_account_c', 'ascent_2_ff_purchase_order_c', 'c_2_g_invoice_currency_c', 'c_2_g_due_date_c', 'c_2_g_invoice_date_c', 'approval_date_c', '_fivetran_synced', 'is_deleted'], 

'account': 
	['id', 'account_number_new_c', 'name', 'first_name', 'last_name', 'person_email', 'agent_c', 'account_quality_c', 'status_c', 'association_c', 'partnership_c', 'ust_id_number_c', 'e_shop_dealer_c', 'item_category_c', 'pre_order_ss_16_c', 'billing_street', 'billing_postal_code', 'billing_city', 'billing_state', 'shipping_name_c', 'shipping_street', 'shipping_postal_code', 'shipping_city', 'shipping_state', 'customer_language_c', 'gender_pc', 'type', 'collection_status_c', 'lead_collection_status_update_c', 'comment_collection_status_c', 'on_tech_rep_c', 'gln_c', 'operating_model_c', 'key_account_c', 'risk_profile_c', 'corona_action_proposal_c', 'customer_request_c', 'why_not_active_c', 'c_2_g_codaaccounts_payable_control_c', 'c_2_g_codadefault_expense_account_c', 'c_2_g_codabase_date_1_c', 'c_2_g_codatax_calculation_method_c', 'c_2_g_codainput_vatcode_c', 'payment_system_c', 'c_2_g_codapayment_method_c', 'c_2_g_codabank_name_c', 'c_2_g_codabank_sort_code_c', 'c_2_g_codabank_account_name_c', 'c_2_g_codabank_account_number_c', 'bank_clearing_number_c', 'c_2_g_codabank_ibannumber_c', 'c_2_g_codabank_swiftnumber_c', 'account_number_new_c', 'parent_id', 'record_type_id', 'pbsi_account_group_c', 'owner_id', 'on_payment_term_c', 'on_payment_terms_pre_order_c', 'pw_ccpro_billing_country_lookup_c', 'pw_ccpro_shipping_country_lookup_c', '{{ null_if  agent_lookup_c  }}', 'c_2_g_codaoutput_vatcode_c', 'c_2_g_codacredit_manager_c', 'c_2_g_codafinance_contact_c', 'account_channel_lookup_c', 'c_2_g_codadimension_1_c', 'c_2_g_codadimension_2_c', 'account_balance_new_c', 'account_overdue_balance_c', 'c_2_g_codacredit_limit_c', 'avg_days_overdue_c', 'Shoes_sold_p_a_all_brands_c', 'pbsi_standard_discount_c', 'pre_order_discount_c', 'Budget_1_Qu_2015_c', 'Budget_2_Qu_2015_c', 'bg_fw_17_c', 'bg_fw_17_prg_c', 'ffps_cust_rem_last_reminder_severity_level_c', 'dealer_latitude_c', 'dealer_Longitude_c', 'is_newsletter_subscriber_c', 'person_has_opted_out_of_email', 'referrer_c', 'ffps_cust_rem_exclude_from_reminder_process_c', 'using_aot_system_c', 'created_date', 'ffps_onagdl_dunning_date_c', 'first_order_date_c', 'ffps_cust_rem_last_reminder_generated_date_c', 'ffps_cust_rem_reminders_blocked_until_date_c', 'ffps_cust_rem_last_statement_generated_date_c', 'last_collection_status_update_c', 'nps_c', 'nps_c2', 'ran_customer_c', '_fivetran_synced', 'is_deleted'], 

'atp_c': 
	['id', 'name', 'item_c', 'location_c', 'inventory_c', 'current_atp_c', 'av_date_atp_c', 'availability_date_c', 'current_atp_last_calculated_at_c', 'av_date_atp_last_calculated_at_c', '_fivetran_synced', 'is_deleted'], 

'c_2_g_coda_year_c': 
	['id', 'name', 'c_2_g_status_c', 'c_2_g_owner_company_c', 'c_2_g_start_date_c', 'c_2_g_end_date_c', 'is_deleted'], 

'owner_card_c': 
	['id', 'name', 'other_activities_c', 'other_goals_c', 'product_c', 'purchased_from_c', 'goals_for_the_year_c', 'terrain_c', 'terrain_picklist_c', 'weekly_distance_c', 'product_color_c', 'product_size_c', 'account_c', 'purchased_from_dealer_c', 'first_on_product_c', 'owner_card_registration_date_c', 'created_date', '_fivetran_synced', 'is_deleted', 'test_field']

}
```
