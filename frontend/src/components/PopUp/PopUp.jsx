import React from 'react';

function PopUp({showPopUp, closePopUp, children}){
  if (!showPopUp) {return null}
  return (
    <div className="PopUp" >
        <button onClick={closePopUp}>close</button>
        {children}
    </div>
  );
};

export default PopUp;