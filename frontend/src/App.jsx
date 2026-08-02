import './App.css';
import { useState } from 'react';

import PopUp from './components/PopUp/PopUp';
import ApplicationsTable from './components/ApplicationsTable/ApplicationsTable';
import CreateApplicationForm from './components/CreateApplicationForm/CreateApplicationForm';
import UpdateStatusModal from './components/UpdateStatusModal/UpdateStatusModal';

function App() {
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [refreshKey, setRefreshKey] = useState(0);
  const [selectedApplication, setSelectedApplication] = useState(null);

  const handleApplicationCreated = () => {
    setShowCreateModal(false);
    setRefreshKey((prev) => prev + 1);
  };

  const handleApplicationSelected = (application) => {
    setSelectedApplication(application);
  };

  const handleStatusModalClosed = () => {
    setSelectedApplication(null);
  };

  return (
    <>
      <h1>JobFlow</h1>

      <button onClick={() => setShowCreateModal(true)}>
        Add New Application
      </button>

      <PopUp
        showPopUp={showCreateModal}
        closePopUp={() => setShowCreateModal(false)}
      >
        <CreateApplicationForm
          onSuccess={handleApplicationCreated}
          onCancel={() => setShowCreateModal(false)}
        />
      </PopUp>

      <PopUp
        showPopUp={selectedApplication !== null}
        closePopUp={() => setSelectedApplication(null)}
      >
        <UpdateStatusModal
          selectedApplication={selectedApplication}
          onSuccess={() => {
            setSelectedApplication(null);
            setRefreshKey((prev) => prev + 1);
          }}
          onCancel={() => setSelectedApplication(null)}
        />
      </PopUp>

      <ApplicationsTable
        refreshTrigger={refreshKey}
        onApplicationSelected={handleApplicationSelected}
      />
    </>
  );
}

export default App;