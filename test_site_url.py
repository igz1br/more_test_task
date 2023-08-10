import requests
import pytest
from conftest import urls_list


@pytest.mark.parametrize("url", urls_list)
def test_response_ok(url: str): 
    response = requests.get(url)
    status = response.status_code
    if status != 200:
        with open('wrong_status.txt', 'a') as output_file:
            output_file.write(url+' - '+str(status)+'\n')

@pytest.mark.parametrize("url", urls_list)
def test_canonical_url(url: str, regexp):
    response = requests.get(url)
    if response.status_code == 200:
        canonical_match = regexp.search(response.text)
        if canonical_match:
            canonical_url = canonical_match.group(1)
            if url != canonical_url:
                with open('noncanonical_url.txt', 'w+') as output_file:
                    output_file.writelines([url+'-'+canonical_url])
                assert url == canonical_url