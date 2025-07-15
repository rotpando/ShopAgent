#!/bin/bash

# ShopAgent Docker Setup Script
# This script helps you set up and run the ShopAgent project with Docker

echo "🐳 ShopAgent Docker Setup"
echo "========================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if docker-compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Setup Groq (free LLM)
echo ""
echo "🤖 Setting up FREE LLM (Groq)..."
echo "We'll use Groq - it's fast, free, and perfect for learning!"
echo ""

# Check if .env already exists
if [ -f .env ]; then
    echo "⚠️  .env file already exists."
    read -p "Do you want to reconfigure? (y/n): " reconfigure
    if [ "$reconfigure" = "y" ]; then
        ./setup-groq.sh
    fi
else
    ./setup-groq.sh
fi

# Build the Docker image
echo ""
echo "🏗️  Building Docker image..."
docker-compose build

# Download dataset inside container
echo "📦 Downloading dataset..."
docker-compose run --rm shopagent python3 download_dataset.py

# Build vector database inside container
echo "🔍 Building vector database..."
docker-compose run --rm shopagent python3 src/build_vector_db.py

# Start the application
echo "🚀 Starting ShopAgent..."
docker-compose up -d

echo ""
echo "✅ ShopAgent is running!"
echo "🌐 Access the app at: http://localhost:8501"
echo ""
echo "💰 Using Groq (FREE & FAST):"
echo "   🚀 Speed: Very fast inference"
echo "   💰 Cost: 100% FREE"
echo "   🤖 Model: Llama 3.1 8B"
echo ""
echo "Useful commands:"
echo "  docker-compose logs -f shopagent    # View logs"
echo "  docker-compose down                 # Stop the app"
echo "  docker-compose restart shopagent    # Restart the app"
echo "  docker-compose exec shopagent bash  # Enter container shell"
echo ""
echo "🎉 Happy coding! Your free AI assistant is ready!" 