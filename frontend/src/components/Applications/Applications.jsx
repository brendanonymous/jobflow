import "./Applications.css"
import { useState, useEffect } from "react"
import { fetchApplications } from "../../api/applications";

export default function Applications() {
    const [applications, setApplications] = useState([]);
    
    async function loadApplications() {
        const data = await fetchApplications();
        setApplications(data);
    }

    useEffect(() => {
        loadApplications();
    }, [])

    console.log(applications[0]);
    
    const listOfApplications = applications.map(application => (
        <tr key={application.id}>
            <td>{application.company_name}</td>
            <td>{application.role_name}</td>
            <td>{application.applied_date}</td>
            {/* <td>{application.status_events.at(-1)?.status}</td> */}
        </tr>
    ));

    return (
        <table>
            <thead>
                <tr>
                    <th>Company</th>
                    <th>Role</th>
                    <th>Date Applied</th>
                    <th>Current Status</th>
                </tr>
            </thead>
            <tbody>
                {listOfApplications}
            </tbody>
        </table>
    );
}