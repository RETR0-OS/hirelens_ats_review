from django.db import models

class ResumeReview(models.Model):
    """
    Model to store resume review data.
    """
    resume_parsed_text = models.TextField(help_text="The parsed text of the resume reviewed.", null=True, blank=True)
    resume_file = models.FileField(upload_to='resumes/', help_text="The original resume file uploaded by the user.")
    overall_score = models.FloatField(default=0.0, help_text="Overall score of the resume review.", null=True, blank=True)
    overall_feedback = models.TextField(help_text="Overall feedback provided by the reviewer.", null=True, blank=True)

    resume_stats = models.TextField(help_text="Statistics of the resume review.", null=True, blank=True)

    sections_found = models.TextField(help_text="Sections found in the resume.", null=True, blank=True)
    missing_sections = models.TextField(help_text="Sections that are missing in the resume.", null=True, blank=True)

    issues_found = models.TextField(help_text="Issues found in the resume.", null=True, blank=True)

    keyword_match_score = models.FloatField(default=0.0, help_text="Score based on keyword matching in the resume.", null=True, blank=True)

    recommendations = models.TextField(help_text="Recommendations for improving the resume.", null=True, blank=True)