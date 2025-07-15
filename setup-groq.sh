#!/bin/bash

# Simple setup script for Groq (Free LLM)
echo "🚀 Setting up Groq (Free & Fast LLM)"
echo "====================================="
echo ""
echo "Groq provides FREE access to fast LLM models!"
echo "No credit card required, just sign up."
echo ""
echo "📝 Steps:"
echo "1. Go to: https://groq.com"
echo "2. Sign up for free"
echo "3. Go to API Keys section"
echo "4. Create a new API key"
echo "5. Enter it below:"
echo ""

read -p "Enter your Groq API key: " groq_key

if [ -z "$groq_key" ]; then
    echo "❌ API key cannot be empty"
    exit 1
fi

# Create .env file
echo "📝 Creating .env file..."
cp env.example .env
sed -i.bak "s/your-groq-api-key-here/${groq_key}/" .env
rm .env.bak

echo ""
echo "✅ Groq configured successfully!"
echo "📁 Configuration saved to .env"
echo ""
echo "🎉 Benefits of using Groq:"
echo "   💰 Cost: 100% FREE"
echo "   🚀 Speed: Super fast inference"
echo "   🤖 Models: Llama 3.1, Mixtral, Gemma"
echo "   🔄 API: OpenAI compatible"
echo ""
echo "🐳 Next steps:"
echo "1. Run: docker-compose up --build"
echo "2. Open: http://localhost:8501"
echo "3. Start chatting with your free AI assistant!"
echo ""
echo "💡 Tip: Groq has generous free limits, perfect for learning!" 