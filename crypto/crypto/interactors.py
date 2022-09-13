def calculate_ytd_statistics(username):
    return {
        'min': _get_ytd_min(username),
        'max': _get_ytd_max(username),
        'performance': _get_ytd_performance(username),
    }


def _get_ytd_min(username):
    return 0


def _get_ytd_max(username):
    return 10000000


def _get_ytd_performance(username):
    return 100000

