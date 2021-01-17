import React, { createContext, useState } from "react";

export const IsSuperUserContext = createContext();

export const LoggedInContextProvider = (props) => {
    const [isSuperUser, setIsSuperUser] = useState(localStorage.getItem("is_superuser")=="true");

    return(
        <IsSuperUserContext.Provider value={[isSuperUser, setIsSuperUser]}>
            {props.children}
        </IsSuperUserContext.Provider>
    )

}