import { useEffect } from 'react';
import isEqual from 'lodash/isEqual';
import useGetPermissions from './useGetPermissions';
import { useSafeSetState } from '../util/hooks';
var emptyParams = {};
// keep a cache of already fetched permissions to initialize state for new
// components and avoid a useless rerender if the permissions haven't changed
var alreadyFetchedPermissions = { '{}': [] };
/**
 * Hook for getting user permissions without the loading state.
 *
 * When compared to usePermissions, this hook doesn't cause a re-render
 * when the permissions haven't changed since the last call.
 *
 * This hook doesn't handle the loading state.
 *
 * @see usePermissions
 *
 * Calls the authProvider.getPermissions() method asynchronously.
 * If the authProvider returns a rejected promise, returns empty permissions.
 *
 * The return value updates according to the request state:
 *
 * - start:   { permissions: [previously fetched permissions for these params] }
 * - success: { permissions: [permissions returned by the authProvider (usually the same as on start)] }
 * - error:   { error: [error from provider] }
 *
 * Useful to enable features based on user permissions
 *
 * @param {Object} params Any params you want to pass to the authProvider
 *
 * @returns The current auth check state. Destructure as { permissions, error }.
 *
 * @example
 *     import { usePermissionsOptimized } from 'react-admin';
 *
 *     const PostDetail = props => {
 *         const { permissions } = usePermissionsOptimized();
 *         if (permissions !== 'editor') {
 *             return <Redirect  to={`posts/${props.id}/show`} />
 *         } else {
 *             return <PostEdit {...props} />
 *         }
 *     };
 */
var usePermissionsOptimized = function (params) {
    if (params === void 0) { params = emptyParams; }
    var _a = useSafeSetState({
        permissions: alreadyFetchedPermissions[JSON.stringify(params)],
    }), state = _a[0], setState = _a[1];
    var getPermissions = useGetPermissions();
    useEffect(function () {
        getPermissions(params)
            .then(function (permissions) {
            var key = JSON.stringify(params);
            if (!isEqual(permissions, alreadyFetchedPermissions[key])) {
                alreadyFetchedPermissions[key] = permissions;
                setState({ permissions: permissions });
            }
        })
            .catch(function (error) {
            setState({
                error: error,
            });
        });
    }, [getPermissions, params, setState]);
    return state;
};
export default usePermissionsOptimized;
