from pydantic import BaseModel, HttpUrl
from typing import Optional, List


# # # # PROFILE ITEMS # # # #

class DateItem(BaseModel):
    day: Optional[int]
    month: Optional[int]
    year: Optional[int]


class ProfileExperienceItem(BaseModel):
    starts_at: Optional[DateItem]
    ends_at: Optional[DateItem]
    company: Optional[str]
    company_linkedin_profile_url: Optional[str]
    title: Optional[str]
    description: Optional[str]
    location: Optional[str]
    logo_url: Optional[str]


class ProfileEducationItem(BaseModel):
    starts_at: Optional[DateItem]
    ends_at: Optional[DateItem]
    field_of_study: Optional[str]
    degree_name: Optional[str]
    school: Optional[str]
    school_linkedin_profile_url: Optional[str]
    description: Optional[str]
    logo_url: Optional[str]
    grade: Optional[str]
    activities_and_societies: Optional[str]


class ProfileAccomplishmentsItem(BaseModel):
    name: Optional[str]
    number: Optional[str]


class ProfilePeopleAlsoViewedItem(BaseModel):
    link: Optional[str]
    name: Optional[str]
    summary: Optional[str]
    location: Optional[str]


# # # # COMPANY ITEMS # # # #


class CompanyLocationItem(BaseModel):
    city: Optional[str]
    country: Optional[str]
    postal_code: Optional[str]
    line_1: Optional[str]
    is_hq: Optional[bool]
    state: Optional[str]

    class Config:
        remove_none = True


class UpdatePostedOnItem(BaseModel):
    day: Optional[int]
    month: Optional[int]
    year: Optional[int]


class CompanyUpdateItem(BaseModel):
    article_link: Optional[str]
    posted_on: Optional[UpdatePostedOnItem]
    text: Optional[str]
    total_likes: Optional[int]


class SimilarCompaniesItem(BaseModel):
    industry: Optional[str]
    link: Optional[str]
    location: Optional[str]
    name: Optional[str]


class CompanySocialMediaItem(BaseModel):
    service: Optional[str]
    canonical_url: Optional[str]
    internal_id: Optional[str]


class CompanyExtraItem(BaseModel):
    ipo_status: Optional[str]
    crunchbase_rank: Optional[int]
    founding_date: Optional[DateItem]
    operating_status: Optional[str]
    contact_email: Optional[str]
    phone_number: Optional[str]
    facebook_id: Optional[str]
    twitter_id: Optional[str]
    number_of_funding_rounds: Optional[int]
    total_funding_amount: Optional[int]
    stock_symbol: Optional[str]
    ipo_date: Optional[DateItem]
    number_of_lead_investors: Optional[int]
    number_of_investors: Optional[int]
    total_fund_raised: Optional[int]
    number_of_investments: Optional[int]
    number_of_lead_investments: Optional[int]
    number_of_exits: Optional[int]
    number_of_acquisitions: Optional[int]


# # # # JOB ITEMS # # # #

class JobListingsItem(BaseModel):
    company: str
    company_url: str
    job_title: str
    job_url: str
    list_date: Optional[str]
    location: Optional[str]


class JobDescriptionItem(BaseModel):
    employment_type: Optional[str]
    seniority_level: Optional[str]
    industry: Optional[List[str]]
    location: Optional[CompanyLocationItem]
    job_description: Optional[str]
    job_functions: Optional[List[str]]
    title: Optional[str]
    total_applicants: Optional[int]


# # # # SEARCH ITEMS # # # #

class SearchResponseItem(BaseModel):
    title: str
    snippet: str
    position: int
    link: HttpUrl

    class Config:
        orm_mode = False

class SearchLookupTermItem(BaseModel):
    company: str = "linkedin.com/company/"
    person: str = "linkedin.com/in/"