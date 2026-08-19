CLICK_INTERVAL = 0.2  # Time interval between clicks in seconds

# Define the maximum and minimum click intervals for validation
MIN_CLICK_INTERVAL = 0.1  # Minimum interval allowed
MAX_CLICK_INTERVAL = 5.0  # Maximum interval allowed

# Click types that can be defined for the autoclicker
CLICK_TYPES = {
    'left': 'left',
    'right': 'right',
    'middle': 'middle'
}

# Default settings for the autoclicker
DEFAULT_SETTINGS = {
    'click_type': CLICK_TYPES['left'],
    'click_interval': CLICK_INTERVAL,
    'click_count': 100,
    'active': True
}

# Error messages for validation
def get_error_messages():
    return {
        'invalid_click_type': 'Invalid click type specified.',
        'interval_out_of_bounds': 'Click interval must be between {} and {} seconds.'.format(MIN_CLICK_INTERVAL, MAX_CLICK_INTERVAL)
    }

# Function to validate settings for the autoclicker
def validate_settings(settings):
    if settings['click_interval'] < MIN_CLICK_INTERVAL or settings['click_interval'] > MAX_CLICK_INTERVAL:
        raise ValueError(get_error_messages()['interval_out_of_bounds'])
    if settings['click_type'] not in CLICK_TYPES.values():
        raise ValueError(get_error_messages()['invalid_click_type'])
    return True