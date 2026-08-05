import { useEffect } from "react";
import { useAuth } from "react-oidc-context";

function Callback() {
  const auth = useAuth();

  useEffect(() => {
    // Cognito redirects here with auth code
    // react-oidc-context handles the exchange automatically
    if (auth.isAuthenticated) {
      window.location.href = "/";
    }
  }, [auth.isAuthenticated]);

  return <div>Processing login...</div>;
}

export default Callback;