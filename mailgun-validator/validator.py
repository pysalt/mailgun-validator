from typing import List

REQUEST_TIMEOUT = 10
API_KEY = ''  # todo move to config
VALIDATION_URL = 'https://api.mailgun.net/v4/address/validate'  # todo move to config

VALIDATION_ERRORS_REASONS = {
    'unknown_provider':	'The MX provider is an unknown provider.',
    'no_mx': 'The recipient domain does not have a valid MX host.',
    'No MX host found': 'The recipient domain does not have a valid MX host.',
    'high_risk_domain': 'Information obtained about the domain indicates it is high risk to send email to.',
    'subdomain_mailer': 'The recipient domain is identified to be a subdomain and is not on our exception list.',
    'immature_domain':	'The domain is newly created based on the WHOIS information.',
    'tld_risk': 'The domain has a top-level-domain (TLD) that has been identified as high risk.',
    'mailbox_does_not_exist': 'The mailbox is undeliverable or does not exist.',
    'mailbox_is_disposable_address': 'The mailbox has been identified to be a disposable address.',
    'mailbox_is_role_address': 'The mailbox is a role based address (ex. support@…, marketing@…).',
}


class EmailValidator:
    def __init__(self, email):
        """
        :param email: email to validate
        """
        self.email = email
        self._validation_errors = []
        self._email_is_valid = True

    @property
    def validation_errors(self) -> List[str]:
        """
        Return email invalid reason list
        :return: list of reasons
        """
        return self._validation_errors

    def validate(self) -> bool:
        """
        Validate email in Mailgun API
        :return:
        """
        pass
