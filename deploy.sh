#!/bin/bash

# SkillsContinua Deployment Script
# For Ubuntu/Debian servers

echo "🚀 Starting SkillsContinua Deployment..."
echo "========================================="

# Update system
echo "📦 Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install dependencies
echo "📦 Installing dependencies..."
sudo apt install -y python3 python3-pip python3-venv postgresql nginx git

# Clone repository
echo "📁 Cloning repository..."
git clone https://github.com/skillcontinua/skillscontinua.git /var/www/skillscontinua
cd /var/www/skillscontinua

# Create virtual environment
echo "🐍 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python packages
echo "📦 Installing Python packages..."
pip install -r requirements.txt
pip install gunicorn psycopg2-binary

# Set up environment variables
echo "🔐 Setting up environment variables..."
cp .env.example .env
nano .env

# Set up database
echo "🗄️ Setting up database..."
sudo -u postgres psql -c "CREATE DATABASE skillscontinua;"
sudo -u postgres psql -c "CREATE USER skillscontinua_user WITH PASSWORD 'your_password';"
sudo -u postgres psql -c "ALTER ROLE skillscontinua_user SET client_encoding TO 'utf8';"
sudo -u postgres psql -c "ALTER ROLE skillscontinua_user SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE skillscontinua_user SET timezone TO 'Africa/Lagos';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE skillscontinua TO skillscontinua_user;"

# Run migrations
echo "📊 Running migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "👤 Creating superuser..."
python manage.py createsuperuser

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Set permissions
echo "🔒 Setting permissions..."
sudo chown -R www-data:www-data /var/www/skillscontinua

# Set up Gunicorn
echo "⚡ Setting up Gunicorn..."
sudo cp deployment/gunicorn.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl start gunicorn

# Set up Nginx
echo "🌐 Setting up Nginx..."
sudo cp deployment/nginx.conf /etc/nginx/sites-available/skillscontinua
sudo ln -s /etc/nginx/sites-available/skillscontinua /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

echo ""
echo "✅ Deployment complete!"
echo "========================================="
echo "🌍 Visit: https://skillscontinua.com"
echo "🔑 Admin: https://skillscontinua.com/admin"