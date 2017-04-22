angular.module('positions', [])
.controller('getPositions', function($scope, $http) {
    $http.get('http://192.168.0.194:5000/position/5').
        then(function(response) {
            $scope.position = response.data;
        }).
        then($http.get('http://192.168.0.194:5000/positions').
        then(function(response) {
            $scope.positions = response.data;
        }));

$scope.update = function() {
   url = 'http://192.168.0.194:5000/position/'+$scope.selectID.id;
   $http.get(url).
        then(function(response) {
            $scope.position = response.data;
        })
}

});

