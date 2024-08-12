############
#
# Code Review
#
# Please do a code review for the following snippet.
# Add your review suggestions inline as python comments
#
############
def get_value(data, key, default, lookup=None, mapper=None):
    """
    Finds the value from data associated with key, or default if the
    key isn't present.
    If a lookup enum is provided, this value is then transformed to its
    enum value.
    If a mapper function is provided, this value is then transformed
    by applying mapper to it.
    """
    return_value = data[key]  # Use data.get(key, default) in order not to get KeyError in case key is not present
    if return_value is None or return_value == "":
        return_value = default
    if lookup:
        return_value = lookup[return_value]  # Be sure to handle the case with exception when return_value is not found in lookup
    if mapper:
        return_value = mapper(return_value)
    return return_value


def ftp_file_prefix(namespace):
    """
    Given a namespace string with dot-separated tokens, returns the
    string with
    the final token replaced by 'ftp'.
    Example: a.b.c => a.b.ftp
    """
    #  Before moving on check if string does have at least one dot, if there is no
    return ".".join(namespace.split(".")[:-1]) + '.ftp'  # It'll break if there's no dot in the namespace. Add error handling.


def string_to_bool(string):
    """
    Returns True if the given string is 'true' case-insensitive,
    False if it is
    'false' case-insensitive.
    Raises ValueError for any other input.
    """
    #  Trim the whitespaces if they does exist
    if string.lower() == 'true':
        return True
    if string.lower() == 'false':
        return False
    raise ValueError(f'String {string} is neither true nor false')


def config_from_dict(dict):
    """
    Given a dict representing a row from a namespaces csv file,
    returns a DAG configuration as a pair whose first element is the
    DAG name
    and whose second element is a dict describing the DAG's properties
    """
    namespace = dict['Namespace']  # Use .get() to avoid KeyError if 'Namespace' is missing
    return (dict['Airflow DAG'],  # Use .get() to avoid KeyError if 'Airflow DAG' is missing
            {"earliest_available_delta_days": 0,
             "lif_encoding": 'json',
             "earliest_available_time":
                 get_value(dict, 'Available Start Time', '07:00'),
             "latest_available_time":
                 get_value(dict, 'Available End Time', '08:00'),
             "require_schema_match":
                 get_value(dict, 'Requires Schema Match', 'True',
                           mapper=string_to_bool),
             "schedule_interval":
                 get_value(dict, 'Schedule', '1 7 * * * '),
             "delta_days":
                 get_value(dict, 'Delta Days', 'DAY_BEFORE',
                           lookup=DeltaDays),   # Handle potential NameError by ensuring DeltaDays is imported or defined.
             "ftp_file_wildcard":
                 get_value(dict, 'File Naming Pattern', None),
             "ftp_file_prefix":
                 get_value(dict, 'FTP File Prefix',
                           ftp_file_prefix(namespace)),
             "namespace": namespace
             }
            )
