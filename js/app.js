(function(angular) {
  'use strict';

var app = angular.module('revealApp',[]);

app.controller('PaneController', PaneController);
PaneController.$inject = ['$scope']; 

function PaneController($scope) {

    function activate() {
        $scope.items = ['git', 'npm', 'bower'];
        $scope.selection = $scope.items[1];
        console.log($scope);
        $scope.$watch(
            function () {
                return angular.element('.current-fragment').attr("data-selection") || "";
            },
            function (newValue, oldValue) {
                $scope.selection = newValue;
                // $scope.$apply();
            }
        );
    }

    activate();

}

})(window.angular);

