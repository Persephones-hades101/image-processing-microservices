# services/nginx/Dockerfile
FROM nginx:latest

# Remove default nginx config
RUN rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/nginx.conf

# Copy custom nginx config
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# Create directory for storage if it doesn't exist
RUN mkdir -p /storage

EXPOSE 80