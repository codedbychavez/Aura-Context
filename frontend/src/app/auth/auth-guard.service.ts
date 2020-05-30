import { Injectable } from '@angular/core';
import { Router, CanActivate, CanLoad } from '@angular/router'
import { AuthService } from "./auth.service";

@Injectable({
  providedIn: 'root'
})
export class AuthGuardService implements CanActivate {

  constructor(public auth: AuthService, public router: Router) { }

  canActivate() {
    if (this.auth.isLoggedIn()) {
      return true;
    } else {
    this.router.navigate(['login']);
    return false;
    }
    
}

}