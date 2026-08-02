const BASE_URL = "http://localhost:8000"; // TODO: update to env var before deployment

export const fetchApplications = async () => {
  const response = await fetch(`${BASE_URL}/applications`);

  if (!response.ok) {
    throw new Error(`Failed to fetch applications. Status: ${response.status}`);
  }

  return response.json();
};

export const createApplication = async (payload) => {
  const response = await fetch(`${BASE_URL}/applications`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }

  return response.json();
};

export const addStatusEvent = async (applicationId, status) => {
  const response = await fetch(`${BASE_URL}/applications/${applicationId}/status_events`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({status}),
  });

  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${response.status}`);
  }

  return response.json();
};