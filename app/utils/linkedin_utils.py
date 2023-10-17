import random
from urllib.parse import urlparse, urlunparse, urljoin
from random import sample
from typing import List, Optional, Union

class LinkedinUtils:

    def is_valid_url(self, url: str) -> bool:
        """
        Check if URL is valid
        """
        parts = urlparse(url)
        return all([parts.scheme, parts.netloc])

    def is_full_linkedin_url(self, url: str) -> bool:
        """
        Check if URL is a full LinkedIn URL
        """
        parts = urlparse(url)
        return all([parts.scheme, parts.netloc, parts.path]) and 'linkedin.com' in parts.netloc

    def format_url(self, url: str) -> str:
        """
        Given a URL, make sure it includes a scheme (https) and www if not present
        """

        if 'linkedin.com' in url and '://' not in url:
            url = 'https://' + url

        parts = urlparse(url)

        if parts.scheme == "" and 'linkedin.com' in parts.netloc:
            parts = parts._replace(scheme="https")

        if "www." not in parts.netloc and 'linkedin.com' in parts.netloc:
            parts = parts._replace(netloc="www." + parts.netloc)

        return urlunparse(parts).replace(" ", "")

    def get_public_identifier(self, url: str) -> str | None:
        """
        Given a URL, return the final slug
        """
        url = self.format_url(url)
        parts = urlparse(url.rstrip("/"))
        if self.is_valid_url(url):
            if '/in/' in parts.path or '/company/' in parts.path:
                return parts.path.split('/')[-1]
            else:
                raise ValueError("Invalid URL, must be a linkedin profile or company page")
        else:
            return url.strip("/")


    def has_slugs(self, url: str) -> bool:
        """
        Given a URL, return True if it has slugs
        """
        return any(urlparse(url).path.strip("/").split("/"))

    def limit_response_size(self, attrib: List, max_items: int = 10) -> List:
        """
        Given a list of URLs, return a list of unique URLs
        """
        attrib = list(set([url for url in attrib]))
        if len(attrib) > max_items:
            attrib = random.sample(attrib, max_items)
        return attrib

    def generate_url(self, url: str, company: bool = False, profile: bool = False) -> str:
        """
        Given a URL, return a full LinkedIn URL
        """
        url = self.format_url(url)

        if self.is_full_linkedin_url(url):
            return url

        base_url = {
            'company': 'https://www.linkedin.com/company/',
            'profile': 'https://www.linkedin.com/in/',
        }

        if company == profile:
            raise ValueError('Must be either company or profile')

        identifier = self.get_public_identifier(url)
        return base_url["company" if company else "profile"] + identifier

linkedin_utils = LinkedinUtils()



if __name__ == "__main__":

    urls  = ["walidfmustapha", "www.linkedin.com/in/walidfmustapha/", "https://www.linkedin.com/in/walidfmustapha", "https://www.linkedin.com/in/walidfmustapha/"]

    for url in urls:
        print(linkedin_utils.generate_url(url, profile=True))
