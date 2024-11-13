# Stage 1: Building the application
FROM node:18 as build

# Create the working directory
WORKDIR /app

# Copy the dependency files
COPY package*.json ./
RUN npm install

# Copy the source code
COPY . .

# Build the Nuxt application (this will generate the /app/.output/dist folder)
RUN npm run build

# Step 2: Serving with Nginx
FROM nginx:alpine

# Copy static files from build stage to Nginx directory
COPY --from=build /app/.output/public /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
