document.addEventListener('DOMContentLoaded', function () {
  const dropArea = document.getElementById('dropArea');
  const fileInput = document.getElementById('fileInput');
  const browseBtn = document.getElementById('browseBtn');
  const imagePreview = document.getElementById('imagePreview');
  const originalImage = document.getElementById('originalImage');
  const processingOptions = document.getElementById('processingOptions');
  const resultsSection = document.getElementById('resultsSection');
  const resultsContainer = document.getElementById('resultsContainer');
  const loading = document.getElementById('loading');
  const filterBtn = document.getElementById('filterBtn');
  const filterType = document.getElementById('filterType');

  const resizeBtn = document.getElementById('resizeBtn');
  const grayscaleBtn = document.getElementById('grayscaleBtn');

  const widthInput = document.getElementById('width');
  const heightInput = document.getElementById('height');

  let currentFile = null;
  let originalImageUrl = null;

  // Handle drag and drop
  dropArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropArea.style.borderColor = '#4361ee';
    dropArea.style.backgroundColor = 'rgba(67, 97, 238, 0.05)';
  });

  dropArea.addEventListener('dragleave', () => {
    dropArea.style.borderColor = '#6c757d';
    dropArea.style.backgroundColor = 'transparent';
  });

  dropArea.addEventListener('drop', (e) => {
    e.preventDefault();
    dropArea.style.borderColor = '#6c757d';
    dropArea.style.backgroundColor = 'transparent';

    if (e.dataTransfer.files.length) {
      handleFileSelect(e.dataTransfer.files[0]);
    }
  });

  // Handle file input
  browseBtn.addEventListener('click', () => {
    fileInput.click();
  });

  fileInput.addEventListener('change', () => {
    if (fileInput.files.length) {
      handleFileSelect(fileInput.files[0]);
    }
  });

  // Process file selection
  function handleFileSelect(file) {
    if (!file.type.match('image.*')) {
      alert('Please select an image file (JPEG, PNG, etc.)');
      return;
    }

    currentFile = file;

    // Display preview
    const reader = new FileReader();
    reader.onload = function (e) {
      originalImageUrl = e.target.result;
      originalImage.src = originalImageUrl;
      imagePreview.style.display = 'block';
      processingOptions.style.display = 'block';

      // Reset results section
      resultsSection.style.display = 'none';
      resultsContainer.innerHTML = '';
    };
    reader.readAsDataURL(file);
  }

  // Resize button handler
  resizeBtn.addEventListener('click', async () => {
    if (!currentFile) return;

    const width = parseInt(widthInput.value);
    const height = parseInt(heightInput.value);

    if (isNaN(width) || isNaN(height) || width < 50 || height < 50) {
      alert('Please enter valid dimensions (minimum 50px)');
      return;
    }

    await processImage(
      '/resize', // Changed from full URL to just the endpoint
      { width, height },
      `resized_${width}x${height}_${currentFile.name}`,
    );
  });

  // Grayscale button handler
  grayscaleBtn.addEventListener('click', async () => {
    if (!currentFile) return;
    await processImage(
      '/grayscale', // Changed from full URL to just the endpoint
      {},
      `grayscale_${currentFile.name}`,
    );
  });

  filterBtn.addEventListener('click', async () => {
    if (!currentFile) return;
    const selectedFilter = filterType.value;
    console.log('Selected filter:', selectedFilter);
    await processImage(
      '/filter',
      { filter_type: selectedFilter },
      `${selectedFilter}_${currentFile.name}`,
    );
  });

  // Generic image processing function
  async function processImage(endpoint, params, outputFilename) {
    try {
      loading.style.display = 'block';

      const formData = new FormData();
      formData.append('file', currentFile);

      // Add additional parameters
      for (const key in params) {
        formData.append(key, params[key]);
      }

      // Using the correct API endpoint with /api prefix
      const response = await fetch(`/api${endpoint}`, {
        method: 'POST',
        body: formData,
        // Don't set Content-Type header - let the browser set it with the boundary
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(
          errorData.error || `HTTP error! status: ${response.status}`,
        );
      }

      const result = await response.json();
      displayResult(result.saved_path, outputFilename);
    } catch (error) {
      console.error('Error:', error);
      alert(`Error processing image: ${error.message}`);
    } finally {
      loading.style.display = 'none';
    }
  }

  // Display processing result
  function displayResult(imagePath, filename) {
    resultsSection.style.display = 'block';

    const resultCard = document.createElement('div');
    resultCard.className = 'result-card';

    // Corrected image URL - using the storage path directly
    const imgUrl = `/storage/${imagePath.split('/').pop()}`;

    resultCard.innerHTML = `
      <img src="${imgUrl}" alt="Processed Image">
      <p>${filename}</p>
      <a href="${imgUrl}" class="download-btn" download="${filename}">Download</a>
    `;

    resultsContainer.appendChild(resultCard);
  }
});
