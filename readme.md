# Image Processing Microservices

A microservices-based application for processing images with operations like
resizing and grayscale conversion.

## Project Overview

The system consists of multiple microservices working together:

- **Frontend Service**: Web interface for uploading images
- **Grayscale Service**: Converts images to grayscale
- **Resize Service**: Resizes images to specified dimensions
- **Nginx**: Acts as gateway/reverse proxy

## Services

| Service   | Port | Technology  | Endpoint        |
| --------- | ---- | ----------- | --------------- |
| Frontend  | 3000 | HTML/CSS/JS | -               |
| Grayscale | 8001 | FastAPI     | `/grayscale/`   |
| Resize    | 8002 | FastAPI     | `/resize/`      |
| Nginx     | 80   | -           | Routes requests |

## API Endpoints

- `/api/resize` - Resize images (parameters: width, height)
- `/api/grayscale` - Convert images to grayscale
- `/storage/*` - Access processed images

## Getting Started

### Prerequisites

- Docker and Docker Compose

### Installation

1. Clone the repository
2. Run: `docker-compose up -d`
3. Access the application at: `http://localhost`

## Deployment Options

- **Docker Compose**: For local development

  ```sh
  docker-compose up -d
  ```

- **Kubernetes**: For production (see Kubernetes manifests)

## Project Structure

```
image-processing-project/
├── docker-compose.yaml       # For local development
├── docker-compose-user.yaml  # For using pre-built images
├── k8s/                      # Kubernetes manifests
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   ├── grayscale-deployment.yaml
│   └── ...
├── services/
│   ├── frontend/             # Frontend web UI
│   ├── grayscale_service/    # Grayscale conversion service
│   ├── nginx/                # Nginx configuration
│   ├── resize_service/       # Image resizing service
│   └── requirements.txt      # Python dependencies
└── storage/                  # Shared storage for processed images
```

## Usage

1. Access the web interface
2. Upload an image
3. Select processing options
4. Download the processed image
