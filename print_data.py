


def print_pos(each_line):

    PURCHASE_ORDER_NUMBER, DIVISION_CODE_CR_D, PO_APPROVAL_IND_D, PO_APPROVAL_DATE_D, \
    PO_MODIFIED_IND_D, PO_MODIFIED_DATE_D, PO_CANCELLED_IND_D, PO_CANCELLED_DATE_D, \
    PO_VOIDED_IND_D, STATION_MNEMONIC_CODE_D, FILLER_D, REGION_CODE_CR_R, \
    PO_APPROVAL_IND_R, PO_APPROVAL_DATE_R, PO_MODIFIED_IND_R, PO_MODIFIED_DATE_R, \
    PO_CANCELLED_IND_R, PO_CANCELLED_DATE_R, PO_VOIDED_IND_R, STATION_MNEMONIC_CODE_R, \
    FILLER_R, MEGA_ZONE_CODE_CR_M, PO_APPROVAL_IND_M, PO_APPROVAL_DATE_M, \
    PO_MODIFIED_IND_M, PO_MODIFIED_DATE_M, PO_CANCELLED_IND_M, PO_CANCELLED_DATE_M, \
    PO_VOIDED_IND_M, STATION_MNEMONIC_CODE_M, FILLER_M, FLT_OWNER_CODE_CR_F, \
    PO_APPROVAL_IND_F, PO_APPROVAL_DATE_F, PO_MODIFIED_IND_F, PO_MODIFIED_DATE_F, \
    PO_CANCELLED_IND_F, PO_CANCELLED_DATE_F, PO_VOIDED_IND_F, STATION_MNEMONIC_CODE_F, \
    FILLER_F, VEHICLE_COST_AMOUNT, DEAL_CODE, VEH_PVT_DEALER_CODE, \
    PO_ORDER_YEAR, VEHICLE_MAKE_CODE, VEHICLE_MODEL_CODE, VEHICLE_BODY_CODE, \
    VEH_OPTION_INFO, VEHICLE_PACKAGE_CODE_INFO, PO_EXT_INT_TOP_CODE_INFO, VEH_CONTRACT_CODE, \
    VEH_CONTRACT_CYCLE_CODE, VEH_LEASE_TERM_NUMBER, MAKE_MOD_VIN_CODE, PO_INITIATOR_ID_CODE, \
    VEHICLES_INVOICED_NUMBER, VEHICLES_RECEIVED_NUMBER, TOT_VEH_ORDER_NUMBER, PO_ORDER_DATE, \
    PO_DELIVER_BY_DATE, DELIVER_DATE_YYMMDD_KEY, PO_PURCHASE_TYPE, PO_DUP_IND, \
    TOTAL_OPTIONS_NUMBER, BILL_TO_LOCATION_NUMBER_CR, DEL_TO_LOCATION_NUMBER_CR, TRANSFER_TO_LOCATION_NO_CR, \
    PO_VALID_IND, PO_DELIVERING_DEALER_CODE, DELIVER_TO_CITY_NAME, VEH_PVT_IND, \
    MANU_CLASS_CODE, PO_TRANS_STATUS_IND, MFR_DEL_TO_LOC_CODE, FON_CANCELLED_COUNT, \
    FILLER_1X_1, MSO_PROCESS_COUNT, FON_LAST_UPDATE_DATE, ITEM_NUM_STAT_IND_INFO, \
    ACKS_RECEIVED_COUNT, TRANSMITTED_DATE, TRANSMITTED_TIME, PRIORITY_LEAD_TIME, \
    MANUFACTURER_CODE_QUICK_SPEC_CODE, BODY_SUFFIX_CODE_QUICK_SPEC_CODE, FINANCE_ALLOWANCE_INFO, MFR_DEALER_CODE, \
    PVT_ADVICE_INDICATOR, MANUFACTURER_CODE_ENGINE_INFO, BODY_SUFFIX_CODE_ENGINE_INFO, MANUFACTURER_CODE_TIRE_INFO, \
    BODY_SUFFIX_CODE_TIRE_INFO, LAST_TRANS_TYPE_CODE, NON_STANDARD_PRIORITY_IND, WEEK_PRIORITY_IND, \
    MONTH_PRIORITY_IND, COUNTRY_CODE, PO_DEPRECIATION_AMOUNT, PO_DEPRECIATION_RATE, \
    PO_BUYBACK_CODE, RETAIL_VEHICLE_COST_AMOUNT, GM_STANDARD_PROD_WEEK_NO, MONDAY_BUILD_WEEK_NO, \
    VEHICLE_TYPE_CODE, DEALER_ZONE_CODE, INTL_PLATE_COST_PU_AMT, INTL_AGE_NUMBER, \
    EMISSION_CODE, EDIT_OVERRIDE, YEAR_PRIORITY_IND, PO_DISPOSAL_DATE, \
    CALIFORNIA_EMISSIONS_IND, SERVICE_VEHICLE_IND, USE_CODE_MODIFY_DATE, VEHICLE_BODY_STYLE_CODE, \
    WIZARD_COLOR_CODE, DISPOSAL_TERM_NUMBER, GM_ORD_THRU_BUS_ASSOC_CD, GM_ORD_THRU_BUS_FUNC_CD, \
    GM_DEAL_BUS_ASSOC_CD, GM_DEAL_BUS_FUNC_CD, GM_DEL_TO_LOC_BUS_ASSOC_CD, GM_DEL_TO_LOC_BUS_FUNC_CD, \
    PRIM_TARG_PROD_DTE, SEC_TARG_PROD_DTE, ORIG_TRANS_DT, ORIG_TRANS_TI, \
    PO_RTRANS_IND, FILLER_42X_1 = each_line.split('~')

    print ('PURCHASE_ORDER_NUMBER--------->{}<----'.format(PURCHASE_ORDER_NUMBER))
    print ('DIVISION_CODE_CR_D--------->{}<----'.format(DIVISION_CODE_CR_D))
    print ('PO_APPROVAL_IND_D--------->{}<----'.format(PO_APPROVAL_IND_D))
    print ('PO_APPROVAL_DATE_D--------->{}<----'.format(PO_APPROVAL_DATE_D))
    print ('PO_MODIFIED_IND_D--------->{}<----'.format(PO_MODIFIED_IND_D))
    print ('PO_MODIFIED_DATE_D--------->{}<----'.format(PO_MODIFIED_DATE_D))
    print ('PO_CANCELLED_IND_D--------->{}<----'.format(PO_CANCELLED_IND_D))
    print ('PO_CANCELLED_DATE_D--------->{}<----'.format(PO_CANCELLED_DATE_D))
    print ('PO_VOIDED_IND_D--------->{}<----'.format(PO_VOIDED_IND_D))
    print ('STATION_MNEMONIC_CODE_D--------->{}<----'.format(STATION_MNEMONIC_CODE_D))
    print ('FILLER_D--------->{}<----'.format(FILLER_D))
    print ('REGION_CODE_CR_R--------->{}<----'.format(REGION_CODE_CR_R))
    print ('PO_APPROVAL_IND_R--------->{}<----'.format(PO_APPROVAL_IND_R))
    print ('PO_APPROVAL_DATE_R--------->{}<----'.format(PO_APPROVAL_DATE_R))
    print ('PO_MODIFIED_IND_R--------->{}<----'.format(PO_MODIFIED_IND_R))
    print ('PO_MODIFIED_DATE_R--------->{}<----'.format(PO_MODIFIED_DATE_R))
    print ('PO_CANCELLED_IND_R--------->{}<----'.format(PO_CANCELLED_IND_R))
    print ('PO_CANCELLED_DATE_R--------->{}<----'.format(PO_CANCELLED_DATE_R))
    print ('PO_VOIDED_IND_R--------->{}<----'.format(PO_VOIDED_IND_R))
    print ('STATION_MNEMONIC_CODE_R--------->{}<----'.format(STATION_MNEMONIC_CODE_R))
    print ('FILLER_R--------->{}<----'.format(FILLER_R))
    print ('MEGA_ZONE_CODE_CR_M--------->{}<----'.format(MEGA_ZONE_CODE_CR_M))
    print ('PO_APPROVAL_IND_M--------->{}<----'.format(PO_APPROVAL_IND_M))
    print ('PO_APPROVAL_DATE_M--------->{}<----'.format(PO_APPROVAL_DATE_M))
    print ('PO_MODIFIED_IND_M--------->{}<----'.format(PO_MODIFIED_IND_M))
    print ('PO_MODIFIED_DATE_M--------->{}<----'.format(PO_MODIFIED_DATE_M))
    print ('PO_CANCELLED_IND_M--------->{}<----'.format(PO_CANCELLED_IND_M))
    print ('PO_CANCELLED_DATE_M--------->{}<----'.format(PO_CANCELLED_DATE_M))
    print ('PO_VOIDED_IND_M--------->{}<----'.format(PO_VOIDED_IND_M))
    print ('STATION_MNEMONIC_CODE_M--------->{}<----'.format(STATION_MNEMONIC_CODE_M))
    print ('FILLER_M--------->{}<----'.format(FILLER_M))
    print ('FLT_OWNER_CODE_CR_F--------->{}<----'.format(FLT_OWNER_CODE_CR_F))
    print ('PO_APPROVAL_IND_F--------->{}<----'.format(PO_APPROVAL_IND_F))
    print ('PO_APPROVAL_DATE_F--------->{}<----'.format(PO_APPROVAL_DATE_F))
    print ('PO_MODIFIED_IND_F--------->{}<----'.format(PO_MODIFIED_IND_F))
    print ('PO_MODIFIED_DATE_F--------->{}<----'.format(PO_MODIFIED_DATE_F))
    print ('PO_CANCELLED_IND_F--------->{}<----'.format(PO_CANCELLED_IND_F))
    print ('PO_CANCELLED_DATE_F--------->{}<----'.format(PO_CANCELLED_DATE_F))
    print ('PO_VOIDED_IND_F--------->{}<----'.format(PO_VOIDED_IND_F))
    print ('STATION_MNEMONIC_CODE_F--------->{}<----'.format(STATION_MNEMONIC_CODE_F))
    print ('FILLER_F--------->{}<----'.format(FILLER_F))
    print ('VEHICLE_COST_AMOUNT--------->{}<----'.format(VEHICLE_COST_AMOUNT))
    print ('DEAL_CODE--------->{}<----'.format(DEAL_CODE))
    print ('VEH_PVT_DEALER_CODE--------->{}<----'.format(VEH_PVT_DEALER_CODE))
    print ('PO_ORDER_YEAR--------->{}<----'.format(PO_ORDER_YEAR))
    print ('VEHICLE_MAKE_CODE--------->{}<----'.format(VEHICLE_MAKE_CODE))
    print ('VEHICLE_MODEL_CODE--------->{}<----'.format(VEHICLE_MODEL_CODE))
    print ('VEHICLE_BODY_CODE--------->{}<----'.format(VEHICLE_BODY_CODE))
    print ('VEH_OPTION_INFO--------->{}<----'.format(VEH_OPTION_INFO))
    print ('VEHICLE_PACKAGE_CODE_INFO--------->{}<----'.format(VEHICLE_PACKAGE_CODE_INFO))
    print ('PO_EXT_INT_TOP_CODE_INFO--------->{}<----'.format(PO_EXT_INT_TOP_CODE_INFO))
    print ('VEH_CONTRACT_CODE--------->{}<----'.format(VEH_CONTRACT_CODE))
    print ('VEH_CONTRACT_CYCLE_CODE--------->{}<----'.format(VEH_CONTRACT_CYCLE_CODE))
    print ('VEH_LEASE_TERM_NUMBER--------->{}<----'.format(VEH_LEASE_TERM_NUMBER))
    print ('MAKE_MOD_VIN_CODE--------->{}<----'.format(MAKE_MOD_VIN_CODE))
    print ('PO_INITIATOR_ID_CODE--------->{}<----'.format(PO_INITIATOR_ID_CODE))
    print ('VEHICLES_INVOICED_NUMBER--------->{}<----'.format(VEHICLES_INVOICED_NUMBER))
    print ('VEHICLES_RECEIVED_NUMBER--------->{}<----'.format(VEHICLES_RECEIVED_NUMBER))
    print ('TOT_VEH_ORDER_NUMBER--------->{}<----'.format(TOT_VEH_ORDER_NUMBER))
    print ('PO_ORDER_DATE--------->{}<----'.format(PO_ORDER_DATE))
    print ('PO_DELIVER_BY_DATE--------->{}<----'.format(PO_DELIVER_BY_DATE))
    print ('DELIVER_DATE_YYMMDD_KEY--------->{}<----'.format(DELIVER_DATE_YYMMDD_KEY))
    print ('PO_PURCHASE_TYPE--------->{}<----'.format(PO_PURCHASE_TYPE))
    print ('PO_DUP_IND--------->{}<----'.format(PO_DUP_IND))
    print ('TOTAL_OPTIONS_NUMBER--------->{}<----'.format(TOTAL_OPTIONS_NUMBER))
    print ('BILL_TO_LOCATION_NUMBER_CR--------->{}<----'.format(BILL_TO_LOCATION_NUMBER_CR))
    print ('DEL_TO_LOCATION_NUMBER_CR--------->{}<----'.format(DEL_TO_LOCATION_NUMBER_CR))
    print ('TRANSFER_TO_LOCATION_NO_CR--------->{}<----'.format(TRANSFER_TO_LOCATION_NO_CR))
    print ('PO_VALID_IND--------->{}<----'.format(PO_VALID_IND))
    print ('PO_DELIVERING_DEALER_CODE--------->{}<----'.format(PO_DELIVERING_DEALER_CODE))
    print ('DELIVER_TO_CITY_NAME--------->{}<----'.format(DELIVER_TO_CITY_NAME))
    print ('VEH_PVT_IND--------->{}<----'.format(VEH_PVT_IND))
    print ('MANU_CLASS_CODE--------->{}<----'.format(MANU_CLASS_CODE))
    print ('PO_TRANS_STATUS_IND--------->{}<----'.format(PO_TRANS_STATUS_IND))
    print ('MFR_DEL_TO_LOC_CODE--------->{}<----'.format(MFR_DEL_TO_LOC_CODE))
    print ('FON_CANCELLED_COUNT--------->{}<----'.format(FON_CANCELLED_COUNT))
    print ('FILLER_1X_1--------->{}<----'.format(FILLER_1X_1))
    print ('MSO_PROCESS_COUNT--------->{}<----'.format(MSO_PROCESS_COUNT))
    print ('FON_LAST_UPDATE_DATE--------->{}<----'.format(FON_LAST_UPDATE_DATE))
    print ('ITEM_NUM_STAT_IND_INFO--------->{}<----'.format(ITEM_NUM_STAT_IND_INFO))
    print ('ACKS_RECEIVED_COUNT--------->{}<----'.format(ACKS_RECEIVED_COUNT))
    print ('TRANSMITTED_DATE--------->{}<----'.format(TRANSMITTED_DATE))
    print ('TRANSMITTED_TIME--------->{}<----'.format(TRANSMITTED_TIME))
    print ('PRIORITY_LEAD_TIME--------->{}<----'.format(PRIORITY_LEAD_TIME))
    print ('MANUFACTURER_CODE_QUICK_SPEC_CODE--------->{}<----'.format(MANUFACTURER_CODE_QUICK_SPEC_CODE))
    print ('BODY_SUFFIX_CODE_QUICK_SPEC_CODE--------->{}<----'.format(BODY_SUFFIX_CODE_QUICK_SPEC_CODE))
    print ('FINANCE_ALLOWANCE_INFO--------->{}<----'.format(FINANCE_ALLOWANCE_INFO))
    print ('MFR_DEALER_CODE--------->{}<----'.format(MFR_DEALER_CODE))
    print ('PVT_ADVICE_INDICATOR--------->{}<----'.format(PVT_ADVICE_INDICATOR))
    print ('MANUFACTURER_CODE_ENGINE_INFO--------->{}<----'.format(MANUFACTURER_CODE_ENGINE_INFO))
    print ('BODY_SUFFIX_CODE_ENGINE_INFO--------->{}<----'.format(BODY_SUFFIX_CODE_ENGINE_INFO))
    print ('MANUFACTURER_CODE_TIRE_INFO--------->{}<----'.format(MANUFACTURER_CODE_TIRE_INFO))
    print ('BODY_SUFFIX_CODE_TIRE_INFO--------->{}<----'.format(BODY_SUFFIX_CODE_TIRE_INFO))
    print ('LAST_TRANS_TYPE_CODE--------->{}<----'.format(LAST_TRANS_TYPE_CODE))
    print ('NON_STANDARD_PRIORITY_IND--------->{}<----'.format(NON_STANDARD_PRIORITY_IND))
    print ('WEEK_PRIORITY_IND--------->{}<----'.format(WEEK_PRIORITY_IND))
    print ('MONTH_PRIORITY_IND--------->{}<----'.format(MONTH_PRIORITY_IND))
    print ('COUNTRY_CODE--------->{}<----'.format(COUNTRY_CODE))
    print ('PO_DEPRECIATION_AMOUNT--------->{}<----'.format(PO_DEPRECIATION_AMOUNT))
    print ('PO_DEPRECIATION_RATE--------->{}<----'.format(PO_DEPRECIATION_RATE))
    print ('PO_BUYBACK_CODE--------->{}<----'.format(PO_BUYBACK_CODE))
    print ('RETAIL_VEHICLE_COST_AMOUNT--------->{}<----'.format(RETAIL_VEHICLE_COST_AMOUNT))
    print ('GM_STANDARD_PROD_WEEK_NO--------->{}<----'.format(GM_STANDARD_PROD_WEEK_NO))
    print ('MONDAY_BUILD_WEEK_NO--------->{}<----'.format(MONDAY_BUILD_WEEK_NO))
    print ('VEHICLE_TYPE_CODE--------->{}<----'.format(VEHICLE_TYPE_CODE))
    print ('DEALER_ZONE_CODE--------->{}<----'.format(DEALER_ZONE_CODE))
    print ('INTL_PLATE_COST_PU_AMT--------->{}<----'.format(INTL_PLATE_COST_PU_AMT))
    print ('INTL_AGE_NUMBER--------->{}<----'.format(INTL_AGE_NUMBER))
    print ('EMISSION_CODE--------->{}<----'.format(EMISSION_CODE))
    print ('EDIT_OVERRIDE--------->{}<----'.format(EDIT_OVERRIDE))
    print ('YEAR_PRIORITY_IND--------->{}<----'.format(YEAR_PRIORITY_IND))
    print ('PO_DISPOSAL_DATE--------->{}<----'.format(PO_DISPOSAL_DATE))
    print ('CALIFORNIA_EMISSIONS_IND--------->{}<----'.format(CALIFORNIA_EMISSIONS_IND))
    print ('SERVICE_VEHICLE_IND--------->{}<----'.format(SERVICE_VEHICLE_IND))
    print ('USE_CODE_MODIFY_DATE--------->{}<----'.format(USE_CODE_MODIFY_DATE))
    print ('VEHICLE_BODY_STYLE_CODE--------->{}<----'.format(VEHICLE_BODY_STYLE_CODE))
    print ('WIZARD_COLOR_CODE--------->{}<----'.format(WIZARD_COLOR_CODE))
    print ('DISPOSAL_TERM_NUMBER--------->{}<----'.format(DISPOSAL_TERM_NUMBER))
    print ('GM_ORD_THRU_BUS_ASSOC_CD--------->{}<----'.format(GM_ORD_THRU_BUS_ASSOC_CD))
    print ('GM_ORD_THRU_BUS_FUNC_CD--------->{}<----'.format(GM_ORD_THRU_BUS_FUNC_CD))
    print ('GM_DEAL_BUS_ASSOC_CD--------->{}<----'.format(GM_DEAL_BUS_ASSOC_CD))
    print ('GM_DEAL_BUS_FUNC_CD--------->{}<----'.format(GM_DEAL_BUS_FUNC_CD))
    print ('GM_DEL_TO_LOC_BUS_ASSOC_CD--------->{}<----'.format(GM_DEL_TO_LOC_BUS_ASSOC_CD))
    print ('GM_DEL_TO_LOC_BUS_FUNC_CD--------->{}<----'.format(GM_DEL_TO_LOC_BUS_FUNC_CD))
    print ('PRIM_TARG_PROD_DTE--------->{}<----'.format(PRIM_TARG_PROD_DTE))
    print ('SEC_TARG_PROD_DTE--------->{}<----'.format(SEC_TARG_PROD_DTE))
    print ('ORIG_TRANS_DT--------->{}<----'.format(ORIG_TRANS_DT))
    print ('ORIG_TRANS_TI--------->{}<----'.format(ORIG_TRANS_TI))
    print ('PO_RTRANS_IND--------->{}<----'.format(PO_RTRANS_IND))
    print ('FILLER_42X_1--------->{}<----'.format(FILLER_42X_1))

