FROM node:current-alpine3.21
WORKDIR /app
COPY /frontend /app
RUN npm install -g live-server
EXPOSE 3000
CMD ["live-server", "--port=3000"]