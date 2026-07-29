import './App.css'
import { useState } from 'react';

import PopUp from './components/PopUp/PopUp';
import Applications from './components/Applications/Applications';
import CreateApplicationForm from './components/CreateApplicationForm/CreateApplicationForm';

// TODO: Update application status
// TODO: Remove an application
// TODO: Button to generate a Sankey visualization
// TODO: Auth
function App() {
  const [showPopUp, setShowPopUp] = useState(false);
  const [refreshKey, setRefreshKey] = useState(0);

  const handleApplicationCreated = () => {
    setShowPopUp(false);
    setRefreshKey((prev) => prev + 1);
  };

  return (
    <>
      <h2>JobFlow</h2>
      <div>
        <button onClick={() => setShowPopUp(true)}>Add New Application</button>
        <PopUp showPopUp={showPopUp} closePopUp={() => setShowPopUp(false)}>
          <CreateApplicationForm
            onSuccess={handleApplicationCreated}
            onCancel={() => setShowPopUp(false)}
          />
        </PopUp>
      </div>
      <Applications refreshTrigger={refreshKey} />
    </>
  );
}

export default App;
