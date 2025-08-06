"""HTML email templates for professional communications."""

HTML_EMAIL_TEMPLATES = {
    "professional_announcement": """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professional Announcement</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
    <div style="border-bottom: 3px solid #007acc; padding-bottom: 20px; margin-bottom: 30px;">
        <h1 style="color: #007acc; margin: 0; font-size: 24px;">[ANNOUNCEMENT TITLE]</h1>
        <p style="margin: 5px 0 0 0; color: #666; font-size: 14px;">[Date]</p>
    </div>
    
    <p style="font-size: 16px; margin-bottom: 20px;">Dear [RECIPIENT_NAME],</p>
    
    <div style="background-color: #f8f9fa; padding: 20px; border-left: 4px solid #007acc; margin-bottom: 25px;">
        <p style="margin: 0; font-weight: bold; color: #007acc;">[KEY MESSAGE OR SUMMARY]</p>
    </div>
    
    <div style="margin-bottom: 25px;">
        <h3 style="color: #333; border-bottom: 1px solid #eee; padding-bottom: 5px;">Details:</h3>
        <ul style="padding-left: 20px;">
            <li>[Detail point 1]</li>
            <li>[Detail point 2]</li>
            <li>[Detail point 3]</li>
        </ul>
    </div>
    
    <div style="background-color: #e8f4f8; padding: 15px; border-radius: 5px; margin-bottom: 25px;">
        <p style="margin: 0;"><strong>Next Steps:</strong></p>
        <p style="margin: 5px 0 0 0;">[What recipients should do next]</p>
    </div>
    
    <p style="margin-bottom: 30px;">If you have any questions, please don't hesitate to reach out.</p>
    
    <div style="border-top: 1px solid #eee; padding-top: 20px; color: #666;">
        <p style="margin: 0;">Best regards,</p>
        <p style="margin: 5px 0 0 0; font-weight: bold;">[YOUR_NAME]</p>
        <p style="margin: 2px 0 0 0;">[YOUR_TITLE]</p>
        <p style="margin: 2px 0 0 0;">[YOUR_CONTACT]</p>
    </div>
</body>
</html>
    """,
    "meeting_invitation": """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meeting Invitation</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
    <div style="text-align: center; background-color: #4a90e2; color: white; padding: 20px; border-radius: 8px; margin-bottom: 30px;">
        <h1 style="margin: 0; font-size: 24px;">Meeting Invitation</h1>
        <p style="margin: 10px 0 0 0; font-size: 18px; font-weight: bold;">[MEETING_TOPIC]</p>
    </div>
    
    <p style="font-size: 16px;">Hi [RECIPIENT_NAME],</p>
    
    <p style="margin-bottom: 25px;">I'd like to schedule a meeting to discuss [MEETING_PURPOSE].</p>
    
    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 25px;">
        <h3 style="margin: 0 0 15px 0; color: #4a90e2;">Meeting Details</h3>
        <table style="width: 100%; border-collapse: collapse;">
            <tr>
                <td style="padding: 8px 0; border-bottom: 1px solid #eee; font-weight: bold; width: 120px;">Date & Time:</td>
                <td style="padding: 8px 0; border-bottom: 1px solid #eee;">[MEETING_DATETIME]</td>
            </tr>
            <tr>
                <td style="padding: 8px 0; border-bottom: 1px solid #eee; font-weight: bold;">Duration:</td>
                <td style="padding: 8px 0; border-bottom: 1px solid #eee;">[DURATION] minutes</td>
            </tr>
            <tr>
                <td style="padding: 8px 0; border-bottom: 1px solid #eee; font-weight: bold;">Location:</td>
                <td style="padding: 8px 0; border-bottom: 1px solid #eee;">[LOCATION_OR_LINK]</td>
            </tr>
            <tr>
                <td style="padding: 8px 0; font-weight: bold;">Attendees:</td>
                <td style="padding: 8px 0;">[ATTENDEE_LIST]</td>
            </tr>
        </table>
    </div>
    
    <div style="margin-bottom: 25px;">
        <h3 style="color: #333; margin-bottom: 10px;">Agenda:</h3>
        <ol style="padding-left: 20px;">
            <li>[Agenda item 1] (X minutes)</li>
            <li>[Agenda item 2] (X minutes)</li>
            <li>[Agenda item 3] (X minutes)</li>
            <li>Next steps and action items (X minutes)</li>
        </ol>
    </div>
    
    <div style="background-color: #fff3cd; border-left: 4px solid #ffc107; padding: 15px; margin-bottom: 25px;">
        <p style="margin: 0;"><strong>Preparation:</strong></p>
        <p style="margin: 5px 0 0 0;">[Any materials to review or prepare beforehand]</p>
    </div>
    
    <div style="text-align: center; margin: 30px 0;">
        <p style="margin-bottom: 15px;">Please confirm your attendance by replying to this email.</p>
        <div style="display: inline-block;">
            <span style="background-color: #28a745; color: white; padding: 10px 20px; border-radius: 5px; margin: 0 5px; text-decoration: none; display: inline-block;">✓ Accept</span>
            <span style="background-color: #dc3545; color: white; padding: 10px 20px; border-radius: 5px; margin: 0 5px; text-decoration: none; display: inline-block;">✗ Decline</span>
        </div>
    </div>
    
    <div style="border-top: 1px solid #eee; padding-top: 20px; color: #666;">
        <p style="margin: 0;">Looking forward to our discussion,</p>
        <p style="margin: 5px 0 0 0; font-weight: bold;">[YOUR_NAME]</p>
    </div>
</body>
</html>
    """,
    "project_update": """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Update</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 25px; border-radius: 10px; margin-bottom: 30px; text-align: center;">
        <h1 style="margin: 0; font-size: 28px;">Project Update</h1>
        <p style="margin: 10px 0 0 0; font-size: 16px; opacity: 0.9;">[PROJECT_NAME] - [UPDATE_PERIOD]</p>
    </div>
    
    <p style="font-size: 16px;">Hi [RECIPIENT_NAME],</p>
    
    <p style="margin-bottom: 25px;">Here's the latest update on [PROJECT_NAME] for [TIME_PERIOD].</p>
    
    <!-- Progress Overview -->
    <div style="background-color: #f8f9fa; border-radius: 8px; padding: 20px; margin-bottom: 25px;">
        <h3 style="margin: 0 0 15px 0; color: #333;">📊 Progress Overview</h3>
        <div style="background-color: #e9ecef; border-radius: 10px; height: 20px; margin-bottom: 10px;">
            <div style="background-color: #28a745; height: 20px; width: [PROGRESS_PERCENT]%; border-radius: 10px; position: relative;">
                <span style="position: absolute; right: 10px; top: 2px; color: white; font-size: 12px; font-weight: bold;">[PROGRESS_PERCENT]%</span>
            </div>
        </div>
        <p style="margin: 0; color: #666; text-align: center;">[PROGRESS_DESCRIPTION]</p>
    </div>
    
    <!-- Achievements -->
    <div style="margin-bottom: 25px;">
        <h3 style="color: #28a745; margin-bottom: 10px;">✅ Completed This [PERIOD]</h3>
        <ul style="padding-left: 20px; margin: 0;">
            <li style="margin-bottom: 5px;">[Achievement 1]</li>
            <li style="margin-bottom: 5px;">[Achievement 2]</li>
            <li style="margin-bottom: 5px;">[Achievement 3]</li>
        </ul>
    </div>
    
    <!-- In Progress -->
    <div style="margin-bottom: 25px;">
        <h3 style="color: #ffc107; margin-bottom: 10px;">🔄 Currently In Progress</h3>
        <ul style="padding-left: 20px; margin: 0;">
            <li style="margin-bottom: 5px;">[In progress item 1]</li>
            <li style="margin-bottom: 5px;">[In progress item 2]</li>
        </ul>
    </div>
    
    <!-- Challenges -->
    <div style="background-color: #fff3cd; border-left: 4px solid #ffc107; padding: 15px; margin-bottom: 25px;">
        <h3 style="margin: 0 0 10px 0; color: #856404;">⚠️ Challenges & Blockers</h3>
        <ul style="margin: 0; padding-left: 20px;">
            <li style="margin-bottom: 5px;">[Challenge 1] - [Resolution plan]</li>
            <li style="margin-bottom: 5px;">[Challenge 2] - [Resolution plan]</li>
        </ul>
    </div>
    
    <!-- Next Steps -->
    <div style="background-color: #e8f4f8; border-radius: 8px; padding: 20px; margin-bottom: 25px;">
        <h3 style="margin: 0 0 15px 0; color: #0056b3;">🎯 Next Steps</h3>
        <table style="width: 100%; border-collapse: collapse;">
            <tr>
                <td style="padding: 8px 0; border-bottom: 1px solid #dee2e6; font-weight: bold; width: 100px;">This Week:</td>
                <td style="padding: 8px 0; border-bottom: 1px solid #dee2e6;">[Next week priorities]</td>
            </tr>
            <tr>
                <td style="padding: 8px 0; border-bottom: 1px solid #dee2e6; font-weight: bold;">Next [PERIOD]:</td>
                <td style="padding: 8px 0; border-bottom: 1px solid #dee2e6;">[Future priorities]</td>
            </tr>
            <tr>
                <td style="padding: 8px 0; font-weight: bold;">Key Dates:</td>
                <td style="padding: 8px 0;">[Important upcoming milestones]</td>
            </tr>
        </table>
    </div>
    
    <!-- Call to Action -->
    <div style="text-align: center; background-color: #007acc; color: white; padding: 15px; border-radius: 8px; margin-bottom: 25px;">
        <p style="margin: 0; font-weight: bold;">Questions or need more details?</p>
        <p style="margin: 5px 0 0 0;">Feel free to reach out or schedule a call to discuss.</p>
    </div>
    
    <div style="border-top: 1px solid #eee; padding-top: 20px; color: #666;">
        <p style="margin: 0;">Thanks for your continued support,</p>
        <p style="margin: 5px 0 0 0; font-weight: bold;">[YOUR_NAME]</p>
        <p style="margin: 2px 0 0 0;">[PROJECT_ROLE]</p>
    </div>
</body>
</html>
    """,
    "newsletter": """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Newsletter</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 0; background-color: #f4f4f4;">
    <!-- Header -->
    <div style="background-color: #2c3e50; color: white; padding: 30px 20px; text-align: center;">
        <h1 style="margin: 0; font-size: 32px; font-weight: bold;">[NEWSLETTER_NAME]</h1>
        <p style="margin: 10px 0 0 0; font-size: 16px; opacity: 0.9;">[TAGLINE_OR_DESCRIPTION]</p>
        <p style="margin: 5px 0 0 0; font-size: 14px; opacity: 0.8;">[DATE] • Issue #[NUMBER]</p>
    </div>
    
    <!-- Content Container -->
    <div style="background-color: white; padding: 30px 20px;">
        
        <!-- Welcome Message -->
        <div style="margin-bottom: 30px; text-align: center; border-bottom: 2px solid #ecf0f1; padding-bottom: 25px;">
            <h2 style="color: #2c3e50; margin: 0 0 15px 0; font-size: 24px;">Hello [SUBSCRIBER_NAME]!</h2>
            <p style="margin: 0; font-size: 16px; color: #7f8c8d;">[WELCOME_MESSAGE_OR_INTRO]</p>
        </div>
        
        <!-- Featured Article -->
        <div style="margin-bottom: 35px;">
            <div style="background: linear-gradient(135deg, #3498db 0%, #2980b9 100%); color: white; padding: 3px 15px; display: inline-block; border-radius: 15px; font-size: 12px; font-weight: bold; text-transform: uppercase; margin-bottom: 15px;">
                ⭐ Featured
            </div>
            <h3 style="margin: 0 0 10px 0; color: #2c3e50; font-size: 20px;">[FEATURED_TITLE]</h3>
            <p style="margin: 0 0 15px 0; color: #7f8c8d; line-height: 1.6;">[FEATURED_EXCERPT]</p>
            <a href="[FEATURED_LINK]" style="background-color: #3498db; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block;">Read More →</a>
        </div>
        
        <!-- News Items -->
        <div style="margin-bottom: 30px;">
            <h3 style="color: #2c3e50; border-bottom: 2px solid #ecf0f1; padding-bottom: 10px; margin-bottom: 20px;">📰 Latest Updates</h3>
            
            <div style="margin-bottom: 20px; padding-bottom: 15px; border-bottom: 1px solid #ecf0f1;">
                <h4 style="margin: 0 0 5px 0; color: #2c3e50; font-size: 16px;">[NEWS_TITLE_1]</h4>
                <p style="margin: 0; color: #7f8c8d; font-size: 14px; line-height: 1.5;">[NEWS_EXCERPT_1]</p>
            </div>
            
            <div style="margin-bottom: 20px; padding-bottom: 15px; border-bottom: 1px solid #ecf0f1;">
                <h4 style="margin: 0 0 5px 0; color: #2c3e50; font-size: 16px;">[NEWS_TITLE_2]</h4>
                <p style="margin: 0; color: #7f8c8d; font-size: 14px; line-height: 1.5;">[NEWS_EXCERPT_2]</p>
            </div>
            
            <div style="margin-bottom: 20px;">
                <h4 style="margin: 0 0 5px 0; color: #2c3e50; font-size: 16px;">[NEWS_TITLE_3]</h4>
                <p style="margin: 0; color: #7f8c8d; font-size: 14px; line-height: 1.5;">[NEWS_EXCERPT_3]</p>
            </div>
        </div>
        
        <!-- Quick Tips -->
        <div style="background-color: #e8f6f3; border-left: 5px solid #16a085; padding: 20px; margin-bottom: 30px; border-radius: 5px;">
            <h3 style="margin: 0 0 15px 0; color: #16a085;">💡 Quick Tip</h3>
            <p style="margin: 0; color: #2c3e50; font-size: 15px; line-height: 1.6;">[TIP_CONTENT]</p>
        </div>
        
        <!-- Upcoming Events -->
        <div style="margin-bottom: 30px;">
            <h3 style="color: #2c3e50; border-bottom: 2px solid #ecf0f1; padding-bottom: 10px; margin-bottom: 20px;">📅 Upcoming Events</h3>
            
            <div style="background-color: #fdf6e3; border: 1px solid #f39c12; border-radius: 8px; padding: 15px; margin-bottom: 15px;">
                <div style="display: table; width: 100%;">
                    <div style="display: table-cell; vertical-align: top; width: 80px; text-align: center; background-color: #f39c12; color: white; padding: 10px; border-radius: 5px; margin-right: 15px;">
                        <div style="font-size: 18px; font-weight: bold;">[DAY]</div>
                        <div style="font-size: 12px;">[MONTH]</div>
                    </div>
                    <div style="display: table-cell; vertical-align: top; padding-left: 15px;">
                        <h4 style="margin: 0 0 5px 0; color: #2c3e50;">[EVENT_TITLE]</h4>
                        <p style="margin: 0; color: #7f8c8d; font-size: 14px;">[EVENT_DESCRIPTION]</p>
                        <p style="margin: 5px 0 0 0; font-size: 12px; color: #95a5a6;">[EVENT_TIME_LOCATION]</p>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Call to Action -->
        <div style="text-align: center; background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); color: white; padding: 25px; border-radius: 10px; margin-bottom: 30px;">
            <h3 style="margin: 0 0 15px 0; font-size: 20px;">[CTA_HEADLINE]</h3>
            <p style="margin: 0 0 20px 0; font-size: 16px; opacity: 0.9;">[CTA_DESCRIPTION]</p>
            <a href="[CTA_LINK]" style="background-color: white; color: #e74c3c; padding: 12px 30px; text-decoration: none; border-radius: 25px; font-weight: bold; font-size: 16px; display: inline-block;">[CTA_BUTTON_TEXT]</a>
        </div>
        
    </div>
    
    <!-- Footer -->
    <div style="background-color: #34495e; color: white; padding: 25px 20px; text-align: center;">
        <p style="margin: 0 0 10px 0; font-size: 16px; font-weight: bold;">[ORGANIZATION_NAME]</p>
        <p style="margin: 0 0 15px 0; font-size: 14px; opacity: 0.8;">[ORGANIZATION_ADDRESS]</p>
        
        <div style="margin-bottom: 15px;">
            <a href="[WEBSITE_LINK]" style="color: #3498db; text-decoration: none; margin: 0 10px;">Website</a>
            <a href="[SOCIAL_LINK_1]" style="color: #3498db; text-decoration: none; margin: 0 10px;">Twitter</a>
            <a href="[SOCIAL_LINK_2]" style="color: #3498db; text-decoration: none; margin: 0 10px;">LinkedIn</a>
        </div>
        
        <div style="border-top: 1px solid #4a5f7a; padding-top: 15px; margin-top: 15px;">
            <p style="margin: 0; font-size: 12px; opacity: 0.7;">
                You're receiving this because you subscribed to [NEWSLETTER_NAME].
                <a href="[UNSUBSCRIBE_LINK]" style="color: #3498db; text-decoration: none;">Unsubscribe</a> | 
                <a href="[PREFERENCES_LINK]" style="color: #3498db; text-decoration: none;">Update preferences</a>
            </p>
        </div>
    </div>
</body>
</html>
    """,
}
