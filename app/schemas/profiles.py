from pydantic import BaseModel, validator
from typing import List, Optional, Any, Union, Dict
import app.schemas.items as items
import app.utils as utils


# # # # DATA MODELS # # # #
class LinkedinProfileItem(BaseModel):  # FIXME: made some Any fields because I couldnt find profiles with these fields populated

    public_identifier: str
    linkedin_url: Optional[str] = None
    profile_pic_url: Optional[str] = None
    background_cover_image_url: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    full_name: Optional[str] = None
    follower_count: Optional[int] = None
    occupation: Optional[str] = None
    headline: Optional[str] = None
    summary: Optional[str] = None
    country: Optional[str] = None
    country_full_name: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    experiences: Optional[List[items.ProfileExperienceItem]] = None
    education: Optional[List[items.ProfileEducationItem]] = None
    languages: Optional[List[str]] = None
    accomplishment_organisations: Optional[List[Any]] = None
    accomplishment_publications: Optional[List[Any]] = None
    accomplishment_honors_awards: Optional[List[Any]] = None
    accomplishment_patents: Optional[List[Any]] = None
    accomplishment_courses: Optional[List[items.ProfileAccomplishmentsItem]] = None
    accomplishment_projects: Optional[List[Any]] = None
    accomplishment_test_scores: Optional[List[Any]] = None
    volunteer_work: Optional[List[Any]] = None
    certifications: Optional[List[Any]] = None
    connections: Optional[Any] = None
    people_also_viewed: Optional[List[items.ProfilePeopleAlsoViewedItem]] = None
    recommendations: Optional[List[Any]] = None
    activities: Optional[List[Any]] = None
    similarly_named_profiles: Optional[List[Any]] = None
    articles: Optional[List[Any]] = None
    groups: Optional[List[Any]] = None
    skills: Optional[List[Any]] = None
    inferred_salary: Optional[Any] = None
    gender: Optional[str] = None
    birth_date: Optional[Any] = None
    industry: Optional[str] = None
    extra: Optional[Any] = None
    interests: Optional[List[Any]] = None
    phone_numbers: Optional[List[Any]] = None
    personal_emails: Optional[List[Any]] = None


    class Config:
        orm_mode = False

    @validator('linkedin_url', pre=True, always=True)
    def generate_linkedin_url_from_public_identifier(cls, v, values):
        print(v, values)
        if v is None and 'public_identifier' in values:
            return utils.linkedin_utils.generate_url(values['public_identifier'], profile=True)
        return v




# # # # REQUEST MODELS # # # #
class GetLinkedinProfilesRequest(BaseModel):
    linkedin_urls: List[str]


# # # # RESPONSE MODELS # # # #


class GetLinkedinProfilesResponse(BaseModel):
    profiles: List[LinkedinProfileItem]

