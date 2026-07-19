# SkillsContinua - Admin Guide

## 🔐 Admin Access

1. Visit `/admin/` on your site
2. Login with superuser credentials
3. Access the admin dashboard

## 📊 Admin Dashboard Sections

### Users
- View all registered users
- Add/edit user profiles
- Manage user roles (learner, instructor, admin)

### Courses
- Add new courses
- Edit existing courses
- Manage course categories
- Set course featured status

### Lessons
- Add lessons to courses
- Upload video content
- Set lesson order
- Mark free preview lessons

### Certificates
- View issued certificates
- Verify certificates
- Generate certificate templates

### Reports
- User activity reports
- Course completion rates
- Certificate statistics

## 📝 Adding Courses

1. Go to Courses → Add Course
2. Fill in: Title, Description, Category, Level
3. Set Learning Approach
4. Upload course image
5. Save and add lessons

## 📖 Adding Lessons

1. Go to the course → Add Lesson
2. Enter Lesson Title and Content
3. Add video URL (YouTube or Vimeo)
4. Set duration and order
5. Save

## 👥 Managing Users

### Roles
- **Learner:** Can browse and enroll in courses
- **Instructor:** Can create and manage courses
- **Admin:** Full system access
- **Mentor:** Can guide learners

### User Actions
- View user profile
- Reset passwords
- Suspend/activate accounts
- View user progress

## 🎓 Managing Certificates

### Issuing Certificates
Certificates are issued automatically when a learner completes a course.

### Verifying Certificates
Anyone can verify a certificate using the verification code.

### Certificate Templates
Customize the certificate design in the admin panel.

## 🛠️ Maintenance Tasks

### Database Backup
Regular backups are essential. Use Django's `dumpdata` command.

### Content Updates
Regularly update course content to keep it fresh.

### User Support
Monitor support requests and respond promptly.

## 🚨 Emergency Procedures

### Site Down
1. Check server status
2. Restart server
3. Check error logs
4. Contact hosting provider

### Security Breach
1. Change all passwords
2. Revoke suspicious sessions
3. Check for unauthorized access
4. Notify affected users

## 📊 Analytics

Monitor key metrics:
- Daily active users
- Course enrollment rates
- Completion rates
- Certificate issuances
- User satisfaction

## 🔒 Security Best Practices

1. Use strong passwords
2. Enable 2FA for admin accounts
3. Regular security audits
4. Keep software updated
5. Monitor access logs

## 📞 Support Channels

- **Email:** support@skillscontinua.com
- **Phone:** [Support Phone]
- **Hours:** 9 AM - 6 PM (Mon-Fri)