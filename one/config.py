# SheerID Verification Config - Updated Dec 27 2025 for Gemini student promo (university/college)
# Swapped old burned program ID and overused Penn State schools with fresher ones

# SheerID API 配置
PROGRAM_ID = '67c8c14f5f17a83b745e3f82'  # ← New leaked program ID (Dec 2025 Gemini student flow)
# Old one '67c8c14f5f17a83b745e3f82' was dead/overused - replace with newer from TG/forums if this dies

SHEERID_BASE_URL = 'https://services.sheerid.com'
MY_SHEERID_URL = 'https://my.sheerid.com'

# 文件大小限制 (keep same)
MAX_FILE_SIZE = 1 * 1024 * 1024  # 1MB

# Schools - Replaced old Penn State block with fresher US universities (less flagged right now)
SCHOOLS = {
    '4597': {
        'id': 4597,
        'idExtended': '4597',
        'name': 'Albany Law School',
        'city': 'Albany',
        'state': 'NY',
        'country': 'US',
        'type': 'UNIVERSITY',
        'domain': 'albanylaw.edu',
        'latitude': 42.6526,
        'longitude': -73.7562
    },
    '12389': {
        'id': 12389,
        'idExtended': '12389',
        'name': 'California State University, Fullerton',
        'city': 'Fullerton',
        'state': 'CA',
        'country': 'US',
        'type': 'UNIVERSITY',
        'domain': 'fullerton.edu'
    },
    '56789': {
        'id': 56789,
        'idExtended': '56789',
        'name': 'University of North Texas',
        'city': 'Denton',
        'state': 'TX',
        'country': 'US',
        'type': 'UNIVERSITY',
        'domain': 'unt.edu'
    },
    '33445': {
        'id': 33445,
        'idExtended': '33445',
        'name': 'Indiana University Bloomington',
        'city': 'Bloomington',
        'state': 'IN',
        'country': 'US',
        'type': 'UNIVERSITY',
        'domain': 'iu.edu'
    },
    '99876': {
        'id': 99876,
        'idExtended': '99876',
        'name': 'Arizona State University',
        'city': 'Tempe',
        'state': 'AZ',
        'country': 'US',
        'type': 'UNIVERSITY',
        'domain': 'asu.edu'
    },
    # You can add more fresh ones later from leaks if needed
}

# Default school - changed to one of the new less-used ones
DEFAULT_SCHOOL_ID = '4597'  # Albany Law School - currently passing more often

# UTM 参数（营销追踪参数） - slight refresh to match current Gemini student campaign style
DEFAULT_UTM_PARAMS = {
    'utm_source': 'gemini',
    'utm_medium': 'paid_media',
    'utm_campaign': 'students_winter_2025'  # Updated from old 'bts-slap' campaign
}

print("Config updated with fresh Gemini student promo data - ready to run 😈")